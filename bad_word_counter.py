"""
This file contains the word_counter_total function, in which a range of years
is inputted and a list of dictionaries containing a count of bad words
per year is outputted.
"""

from get_data import get_table
from song_bad_word_count import song_bad_word


def word_counter_total(start_year, end_year):
    """
    This function is what is run by the user and runs the rest of the functions
    to get the list of dictionaries. It filters through the number of years that
    are inputed and then runs the function get_table for each year. This is outputted
    as a list in a list with two strings in it. First is the artist and second is the song.
    It then runs through the song_bad_word function which converts it to a URL and outputs a
    dictionary with the keys being each bad word and the value being the counter of how
    many times that word appeared. It then appends the dictionary of the single year into the
    all_bad_words. Finally, it raises the year counter and resets the word counter.
    It then repeats this process for each year and at the end returns the list of dictionaries.

    Args:
        start_year: a integer that represents a starting year as early as 1949.
        end_year: a integer that represents a ending year as late as 2022.
    Returns:
        all_bad_words: A list with dictionaries in them. Each dictionary represents a year
        with each key in the dictionary representing a bad word and each value represents the
        counter for number of times this bad word appeared in the top 100 popular songs in that
        year. It also includes a key called year in each dictionary with the specfied year on it.
    """

    # Case for if the start year is greater than the end year
    if end_year < start_year:
        return "end year must be >= start year"
    year = start_year
    # Create the list to be returned
    all_bad_words = []
    while year <= end_year:
        # Get data from get_table function
        year_artist_song = get_table(year)
        # Call song_bad_word function to get the dictionaries
        year_word_counter = song_bad_word(year_artist_song)
        # Add the year to the dictionary
        year_word_counter["year"] = year
        # Append the dictionary into the final list
        all_bad_words.append(year_word_counter)
        # Increase the year
        year += 1
        # Set the dictionary back to empty
        year_word_counter = {}
    return all_bad_words
