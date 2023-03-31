"""
This file contains the song_bad_word function, which counts
the number of bad words in a specific song.
"""

# Import the necessary libraries
from collections import Counter
from genius_lyrics import lyrics


def song_bad_word(year_artist_song):
    """
    This function uses artist and lyrics data and compares it to a word bank
    of bad words and adds the number times each bad word occurs.
    The function uses lyrics which determins the number of bad words in one song.
    The function also uses a Counter function which was imported from collections
    which helps add dictionary values together with the same keys.
    Then returns the answer to how many times each bad word occurs.

    Args:
        year_artist_song: A list with two strings inside them. First is the artist
        and the second is the song name.
    Returns:
        add_dict: A dictionary with each key being each bad word and each value
        being a counter for how many times each bad word occurs.
    """
    # Create dictionary of bad words
    return_dict = Counter(
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
            "hell": 0,
            "cock": 0,
            "penis": 0,
            "bussy": 0,
            "motherfucker": 0,
            "hoe": 0,
            "whore": 0,
            "munch": 0,
        }
    )
    # Generate a URL for each sublist in the main list of 100 songs
    for sublist in year_artist_song:
        url = "https://genius.com/"
        for element in sublist:
            url += element
            url += "-"
        url += "lyrics"
        # Pass the generated URL into the lyrics function
        current_dict = Counter(lyrics(url))
        # Merge the two dictionaries
        return_dict = current_dict + return_dict
    return dict(return_dict)
