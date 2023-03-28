import requests
from bs4 import BeautifulSoup


def lyrics(url):

    soup = BeautifulSoup(requests.get(url).content, "lxml")
    lyrics_text = ""
    bad_word_counter = 0
    bad_word_0 = "fuck"
    bad_word_1 = "bitch"
    bad_word_2 = "shit"
    bad_word_3 = "damn"
    bad_word_4 = "ass"
    bad_word_5 = "sex"

    for tag in soup.select('div[class^="Lyrics__Container"], .song_body-lyrics p'):
        t = tag.get_text(strip=True, separator="\n")
        if t:
            lyrics_text += t + "\n"

    lyrics_list = lyrics_text.split()
    # print(lyrics_list)
    for word in lyrics_list:
        if (
            word.lower() == bad_word_0
            or word.lower() == bad_word_1
            or word.lower() == bad_word_2
            or word.lower() == bad_word_3
            or word.lower() == bad_word_4
            or word.lower() == bad_word_5
        ):
            bad_word_counter += 1
        # print(word)
    return bad_word_counter
