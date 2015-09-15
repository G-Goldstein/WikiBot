from src.wiki_login import wiki_login

with wiki_login('credentials.json') as wiki:
	pagesgot = 0
	for page in wiki.shortestPages():
		pagesgot += 1
		title = page['title']
		content = wiki.contentByTitle(title)
		print title
		if (pagesgot >= 26):  break
		
