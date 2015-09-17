# Wikibot
A Python-based wiki bot

After failing to get Pywikibot working easily, I've created my own wiki bot interface for mediawiki. It's in an early stage but has some working example scripts.

#To use

* Install Python
* Clone this repository.
* Run `get-pip.py`
* Use pip to get the requirements from requirements.txt

Create a 'credentials.json' file in a 'credentials' subdirectory of the root containing a json object as follows:

    {
    	"url":path to the mediawiki's api.php,
    	"lgname":The username of your bot,
    	"lgpassword":The password of your bot,
    	"bot":true or false for whether this account is a bot account
    }
    
Scripts can then be created starting with `from src.wiki_login import wiki_login`. See the examplescripts directory for some examples.
