from genius_lyrics import lyrics
from collections import Counter


def song_bad_word(year_artist_song):
    add_dict = Counter(
        {
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
            "tit": 0,
            "hell": 0,
            "cock": 0,
            "penis": 0,
            "bussy": 0,
            "motherfucker": 0,
            "hoe": 0,
            "whore": 0,
        }
    )

    return_dict = {
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
        "tit": 0,
        "hell": 0,
        "cock": 0,
        "penis": 0,
        "bussy": 0,
        "motherfucker": 0,
        "hoe": 0,
        "whore": 0,
    }
    for sublist in year_artist_song:
        url = "https://genius.com/"
        for element in sublist:
            url += element
            url += "-"
        url += "lyrics"
        current_dict = Counter(lyrics(url))
        add_dict = current_dict + add_dict
        # print(f"add dict: {add_dict}")
        for word in return_dict:
            if word in add_dict:
                return_dict[word] = add_dict[word]
            else:
                return_dict[word] = 0
            # print(f"return dict: {return_dict}")
        # genius_lyrics.py file that returns number of bad words for each song in the year
    print(return_dict)
    return return_dict
