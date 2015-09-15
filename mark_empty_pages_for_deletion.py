from wiki_login import wiki_login

with wiki_login('credentials.json') as wiki:
	for page in wiki.shortestPages():
		title = page['title']
		content = wiki.contentByTitle(title)
		if (len(content) > 0):  break
		wiki.prependTextToPage(title, '{{cmbox|type=delete}}', 'Flagged empty page for deletion', True)
