import requests
from bs4 import BeautifulSoup


def lyrics(url):
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
    }
    soup = BeautifulSoup(requests.get(url).content, "lxml")
    for tag in soup.select('div[class^="Lyrics__Container"], .song_body-lyrics p'):
        for word in tag.get_text(strip=True, separator=" ").split():
            word = word.lower()
            if word in BAD_WORDS:
                BAD_WORDS[word] += 1
    return BAD_WORDS
