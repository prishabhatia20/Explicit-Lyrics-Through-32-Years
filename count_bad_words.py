# from lyricsgenius import Genius
import lyricsgenius as lg

ACCESS_TOKEN = open("access_token.txt", "r", encoding="UTF-8").read().strip()
genius = lg.Genius(
    ACCESS_TOKEN,
    skip_non_songs=True,
    excluded_terms=["(Remix)", "(Live)"],
    remove_section_headers=True,
)


# lyrics = Genius.lyrics(song_title, remove_section_headers=True)


def num_bad_words(song_title, artist_name):
    # song_data = search_song(song_title, n_results = 1, access_token = ACCESS_TOKEN)
    # song = song_data[song_id]
    # lyrics_all = genius.lyrics(song, remove_section_headers=True)
    # print(lyrics_all)

    lyrics_all = ""
    songs = (genius.search_artist(artist_name, max_songs=10, sort="popularity")).songs
    print(songs)
    for song in songs:
        if song == song_title:
            lyrics_all = song.lyrics
            break

    bad_words_counter = 0
    # # search = song_title + " " + artist_name
    # # song = genius.search_songs(search)
    # # lyrics_all = song.lyrics
    bad_words = [
        "fuck",
        "shit",
        "ass",
        "bitch",
        "cunt",
        "dick",
        "sex",
        "slut",
        "pussy",
        "crap",
        "tit",
        "hell",
        "cock",
        "penis",
        "bussy",
    ]
    lyrics = lyrics_all.lower()
    for word in bad_words:
        if word in lyrics:
            bad_words_counter += 1
    return bad_words_counter


    
