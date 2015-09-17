from src.wiki_login import wiki_login

with wiki_login('credentials.json') as wiki:
	with open('lastRevision.csv', 'w') as report:
		report.write('"Page title","Timestamp","User","Unicode error in name or user?"\n')
		for page in wiki.allPages():
			title = page['title']
			revisionLine = wiki.lastMajorRevisionByTitle(title)
			reportString = '"' + revisionLine['title'] + '","' + revisionLine['timestamp'] + '","' + revisionLine['user'] + '"'
			reportStringSafe = ''
			try:
				print(reportString)
				reportStringSafe = reportString + ',""\n'
			except UnicodeEncodeError:
				reportStringSafe = reportString.encode('ascii', 'replace')
				print(reportStringSafe)
				reportStringSafe += ',"Y"\n'
			report.write(reportStringSafe)
