import requests
from bs4 import BeautifulSoup


def lyrics(url):
    """
    This function takes a genius url and requests each url using Beautiful Soups. It then compares
    it to the word bank dictionary, BAD_WORDS with all the bad words defined. It then assigns a counter to each
    bad word that appears in the song. It then returns the dictionary. 

    Args:
        url: A string that is the url to a genius song. 
    Returns:
        BAD_WORDS: a dictionary with each bad word as a key and a counter integer with how many times each
        bad word occured in the song. 
    """
    BAD_WORDS = {
        "fuck": 0,
        "shit": 0,
        "ass": 0,
        "bitch": 0,
        "cunt": 0,
        "dick": 0,
        "sex": 0,
        "slut": 0,
        "pussy": 0,
        "crap": 0,
        "hell": 0,
        "cock": 0,
        "penis": 0,
        "bussy": 0,
        "motherfucker": 0,
        "hoe": 0,
        "whore": 0,
        "munch": 0
    }
    soup = BeautifulSoup(requests.get(url).content, "lxml")
    for tag in soup.select('div[class^="Lyrics__Container"], .song_body-lyrics p'):
        for word in tag.get_text(strip=True, separator=" ").split():
            word = word.lower()
            if word in BAD_WORDS:
                BAD_WORDS[word] += 1
    return BAD_WORDS
