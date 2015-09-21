import unittest
import json
from src.wiki_login import wiki_login
from mock import patch, MagicMock

class TestWikiInit(unittest.TestCase):

	@patch('requests.session')

	def test_init(self, mock_session):
		wikimock = wiki_login
		wikimock._get_credentials = MagicMock()
		wikimock('credtest.json')
		wikimock._get_credentials.assert_called_once_with('credtest.json')
		mock_session.assert_called_once_with()

	#def test_get_credentials(self):
	#	with patch('__builtin__.open') as openmock:
	#		json.loads = MagicMock()
	#		json.loads.return_value = {'url':'http://www.wikipedia.org'}
	#		wikimock = wiki_login
	#		wikimock.

class TestWikiGetCredentials(unittest.TestCase):

	@patch('requests.session')
	@patch('__builtin__.open')
	@patch('json.loads')

	def test_get_credentials_from_object(self, mock_load, mock_open, mock_session):
		wikimock = wiki_login
		wikimock._get_credentials = MagicMock()
		credentialObject = {'url':'www.wikipedia.org', 'lgname':'myName', 'lgpassword':'myPassword','bot':True}
		wikiInstance = wikimock('credtest.json')
		wikiInstance.get_credentials_from_object(credentialObject)
		self.assertEqual(wikiInstance.url, 'www.wikipedia.org')
		self.assertEqual(wikiInstance.lgname, 'myName')
		self.assertEqual(wikiInstance.lgpassword, 'myPassword')
		self.assertEqual(wikiInstance.bot, True)



if __name__ == '__main__':
	unittest.main()