# from lyricsgenius import Genius

# ACCESS_TOKEN = open("access_token.txt", "r").read().strip()
# genius = Genius(ACCESS_TOKEN)

from get_data import get_table
from count_bad_words import num_bad_words


def get_lyrics(year):
    curse_word_count = 0
    lyrics_list = get_table(year)
    for song_title, artist_name in lyrics_list:
        curse_word_count += num_bad_words(song_title, artist_name)
    return curse_word_count


# artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title")
# for song in artist.songs:
#     print(type(song.lyrics))
