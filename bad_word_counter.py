from get_data import get_table
from song_bad_word_count import song_bad_word
def word_counter_total(start_year, end_year):
    year = start_year  
    while year <= end_year:
        year_word_counter = 0
        year_artist_song = get_table(year)
        year_word_counter += song_bad_word(year_artist_song)
        print(f"In {year}, there were {year_word_counter} bad words")
        year += 1
