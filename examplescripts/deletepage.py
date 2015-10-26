from src.wiki_login import wiki_login

with wiki_login('credentials.json') as wiki:
	wiki.delete_page('JUL', 'Nothing on it')