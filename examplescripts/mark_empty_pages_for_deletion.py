#! /usr/local/bin/python3.4

from src.wiki_login import wiki_login

with wiki_login('credentials.json') as wiki:
	for page in wiki.shortestPages():
		title = page['title']
		content = wiki.contentByTitle(title)
		if (len(content) > 0):  break
		wiki.markPageForDeletion(title, 'Flagged empty page for deletion')
