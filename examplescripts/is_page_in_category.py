from src.wiki_login import wiki_login

with wiki_login('credentials.json') as wiki:
	pageIsInCat = wiki.isPageInCategory('RPGUnit', 'Category:RPGUNIT')
	print pageIsInCat