import requests
from bs4 import BeautifulSoup

BAD_WORDS = {"fuck": 0,
        "shit": 0,
        "ass": 0,
        "bitch": 0,
        "cunt": 0,
        "dick": 0,
        "sex": 0,
        "slut": 0,
        "pussy": 0,
        "crap": 0,
        "tit": 0,
        "hell": 0,
        "cock": 0,
        "penis": 0,
        "bussy": 0,
        "munch": 0}

def lyrics(url):
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    bad_word_counter = 0

    for tag in soup.select('div[class^="Lyrics__Container"], .song_body-lyrics p'):
        for word in tag.get_text(strip=True, separator=' ').split():
            word = word.lower()
            if word in BAD_WORDS:
                BAD_WORDS[word] += 1
    return BAD_WORDS

# import requests
# from bs4 import BeautifulSoup


# def lyrics(url):

#     soup = BeautifulSoup(requests.get(url).content, "lxml")
#     lyrics_text = ""
#     bad_word_counter = 0
#     bad_word_0 = "fuck"
#     bad_word_1 = "bitch"
#     bad_word_2 = "shit"
#     bad_word_3 = "damn"
#     bad_word_4 = "ass"
#     bad_word_5 = "sex"
    

#     for tag in soup.select('div[class^="Lyrics__Container"], .song_body-lyrics p'):
#         t = tag.get_text(strip=True, separator="\n")
#         if t:
#             lyrics_text += t + "\n"

#     lyrics_list = lyrics_text.split()
#     # print(lyrics_list)
#     for word in lyrics_list:
#         if (
#             word.lower() == bad_word_0
#             or word.lower() == bad_word_1
#             or word.lower() == bad_word_2
#             or word.lower() == bad_word_3
#             or word.lower() == bad_word_4
#             or word.lower() == bad_word_5
#         ):
#             bad_word_counter += 1
#         # print(word)
#     return bad_word_counter
