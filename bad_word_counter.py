from get_data import get_table
from song_bad_word_count import song_bad_word


def word_counter_total(start_year, end_year):
    year = start_year
    all_bad_words = []
    while year <= end_year:
        year_artist_song = get_table(year)  # all 100 artists + songs
        year_word_counter = song_bad_word(year_artist_song)
        # changes to URL form then goes to lyics function
        all_bad_words.append(year_word_counter)
        print(f"all_bad_words {all_bad_words}")
        year += 1
        year_word_counter = {}
    return all_bad_words
