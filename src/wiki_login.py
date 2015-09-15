import requests
import json

class wiki_login:
	def __init__(self, credentialsFile):
		self._get_credentials(credentialsFile)
		self.session = requests.session()

	def _get_credentials(self, credentialsFile):
		credentialsPath = 'credentials/' + credentialsFile
		with open(credentialsPath) as credentials:
			credentialsObject = json.loads(credentials.read())
			self.getCredentialsFromObject(credentialObject)
			

	def get_credentials_from_object(self, credentialsObject):
		self.url = credentialsObject['url']
		self.lgname = credentialsObject['lgname']
		self.lgpassword = credentialsObject['lgpassword']
		self.bot = credentialsObject['bot']

	def __enter__(self):
		request = {'action':'login', 'format':'json'}
		request['lgname'] = self.lgname
		request['lgpassword'] = self.lgpassword
		result = self.session.post(self.url, params=request).json()
		request['lgtoken'] = result['login']['token']
		result = self.session.post(self.url, params=request).json()
		print 'logged in to %s as %s' % (self.url, self.lgname)
		return self

	def _editToken(self):
		try:
			return self.editToken
		except AttributeError:
			editTokenRequest = {'action':'tokens', 'format':'json'}
			self.editToken = self.session.get(self.url, params=editTokenRequest).json()['tokens']['edittoken']
			return self.editToken

	def __exit__(self, type, value, traceback):
		request = {'action':'logout', 'format':'json'}
		self.session.post(self.url, params=request)
		print 'logged out of %s' % self.url

	def _listquery(self, request):
		request['action'] = 'query'
		request['format'] = 'json'
		request['prop'] = 'revisions'
		request['rvprop'] = 'content'
		lastContinue = {'continue': ''}
		while True:
			req = request.copy()
			req.update(lastContinue)
			result = self.session.get(self.url, params=req).json()
			if 'error' in result: print(result['error'])
			if 'warnings' in result: print(result['warnings'])
			if 'query' in result:
				for page in result['query']['querypage']['results']:
					yield page
			if 'continue' not in result: break
			lastContinue = result['continue']

	def _singlequery(self, request):
		request['action'] = 'query'
		request['format'] = 'json'
		request['prop'] = 'revisions'
		request['rvprop'] = 'content'
		result = self.session.get(self.url, params=request).json()
		for page in result['query']['pages']:
			return result['query']['pages'][page]['revisions'][0]['*'].strip()

	def shortestPages(self):
		return self._listquery({'list':'querypage', 'qppage':'Shortpages'})

	def contentByTitle(self, title):
		request = {'titles': title}
		return self._singlequery(request)

	def prependTextToPage(self, pageTitle, text, summary, minor):
		request = {
			'action':'edit',
			'format':'json',
			'title':pageTitle,
			'bot':self.bot,
			'token':self._editToken(),
			'minor':minor,
			'notminor': not(minor),
			'summary':summary,
			'prependtext':text
		}
		result = self.session.post(self.url, params=request).json()
		print result
