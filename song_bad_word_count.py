from genius_lyrics import lyrics


def song_bad_word(year_artist_song):
    # counter = 0
    for sublist in year_artist_song:
        url = "https://genius.com/"
        for element in sublist:
            url += element
            url += "-"
        url += "lyrics"
        counter_dict = lyrics(
            url
        )  # genius_lyrics.py file that returns number of bad words for each song in the year
    return counter_dict
