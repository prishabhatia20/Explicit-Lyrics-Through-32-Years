"""
This file contains the function get_table, which allows the user
to input a year and get the Wikipedia Billboard Top 100 songs
of that year.
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd


def get_table(year):
    """
    This function returns the Billboard Year-End Hot 100 Singles
    of a user-specified year and returns a list containing the song
    and the artist. The order of the list is the top song to bottom
    song.

    Args:
        year: an integer representing the year the user wants the
        song data from

    Returns:
        list_data: the top 100 data in list format
    """

    # Set the URL to be the link to the article for the year the user specifies
    url = f"https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_{year}"

    # Get the response in URL form
    response = requests.get(url)

    # Parse the data from HTML into a BeautifulSoup object
    parse_data = BeautifulSoup(response.text, "html.parser")
    data_table = parse_data.find("table", {"class": "wikitable"})

    # Convert the Wikipedia table to a dataframe
    data_frame = pd.read_html(str(data_table))
    data_frame = pd.DataFrame(data_frame[0])

    # Drop the first column of the dataframe
    data_frame.drop(columns=data_frame.columns[0], axis=1, inplace=True)

    # Convert the data to a list
    list_data = data_frame.values.tolist()

    # Formatting the list so it follows the formatting of genius.com URLs

    # Removing parentheses
    list_data = [
        [
            item[0].replace("(", "").replace(")", ""),
            item[1].replace(")", "").replace("(", ""),
        ]
        for item in list_data
    ]

    # Replace ampersands with "and"
    list_data = [
        [
            item[0].replace("&", "and").replace("&", "and"),
            item[1].replace("&", "and").replace("&", "and"),
        ]
        for item in list_data
    ]

    # Removing plus signs
    list_data = [
        [
            item[0].replace("+ ", "").replace("+ ", ""),
            item[1].replace("+ ", "").replace("+ ", ""),
        ]
        for item in list_data
    ]

    # Removing quotation marks and backslashes
    list_data = [
        [
            item[0].strip('"\\'),
            item[1].strip('"\\'),
        ]
        for item in list_data
    ]

    list_data = [
        [
            item[0].replace(",", ""),
            item[1].replace(",", ""),
        ]
        for item in list_data
    ]

    # Replacing (x - x) with a single space
    list_data = [
        [
            item[0].replace(" - ", "-").replace(" – ", "-"),
            item[1].replace(" - ", "-").replace(" – ", "-"),
        ]
        for item in list_data
    ]

    # Replace . with nothing
    list_data = [
        [
            item[0].replace(".", ""),
            item[1].replace(".", ""),
        ]
        for item in list_data
    ]

    # Replacing spaces with dashes

    list_data = [
        [item[0].replace(" ", "-"), item[1].replace(" ", "-")] for item in list_data
    ]
    fixed_list = []
    for song, artist in list_data:
        if "featuring" in artist:
            remove_index = artist.index("featuring")
            artist = artist[0 : int(remove_index - 1)]
        fixed_list.append([artist, song])
    return fixed_list
