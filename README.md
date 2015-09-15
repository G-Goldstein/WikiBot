# Wikibot
A Python-based wiki bot

After failing to get Pywikibot working easily, I've created my own wiki bot interface for mediawiki. It's in an early stage but has been used to add a 'delete me' template to all empty pages.

#To use

* Install Python 2.7
* Clone this repository.
* Run `get-pip.py`
* Use pip to get the requirements from requirements.txt

Create a 'credentials.json' file in the same directory as wiki_login.py, containing a json object as follows:

    {
    	"url":path to the mediawiki's api.php,
    	"lgname":The username of your bot,
    	"lgpassword":The password of your bot,
    	"bot":true or false for whether this account is a bot account
    }
    
Scripts can then be created by importing the `wiki_login` object and starting a work block with `with wiki_login('credentials.json') as wiki:`

Maybe I'll put some better examples up in the future.
