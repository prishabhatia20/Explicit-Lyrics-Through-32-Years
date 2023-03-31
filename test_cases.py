"""
Create tests for the get_table function and the lyrics function
"""
import pytest
from get_data import get_table
from genius_lyrics import lyrics

# Define sets of test cases

test_cases_get_table = [
    # Test that the 98th element of the 1990's list
    # is ['Mellow Man Ace', 'Mentirosa']
    (1990, 98, ["Mellow-Man-Ace", "Mentirosa"]),
    # Test that the function removed extra forward slashes
    (1990, 59, ["After-7", "Can't-Stop"]),
    # Test that the function removed extra quotation marks
    (1990, 79, ["Dino", "Romeo"]),
    # Test that the 16th element of the 2000's list
    # is ["Music", "Madonna"]
    (2000, 16, ["Madonna", "Music"]),
    # Test that the 26th element of the 2000's list
    # is ["It's Gonna Be Me", 'N Sync]
    (2000, 26, ["'N-Sync", "It's-Gonna-Be-Me"]),
    # Test that special letters like the squiggly Spanish n
    # show up
    (2020, 43, ["Shawn-Mendes-and-Camila-Cabello", "Señorita"]),
    # Test that parentheses are removed
    (
        1960,
        74,
        [
            "Dinah-Washington-and-Brook-Benton",
            "A-Rockin'-Good-Way-To-Mess-Around-and-Fall-in-Love",
        ],
    ),
    # Test that dashes show up
    (1960, 83, ["Paul-Evans", "Happy-Go-Lucky-Me"]),
    # Test that question marks are removed
    (1970, 25, ["The-Poppy-Family", "Which-Way-You-Goin'-Billy"]),
    # Test that exclamation marks are removed
    (1970, 33, ["John-Lennon", "Instant-Karma"]),
    # Test the 61st element of the 1970s list
    (1970, 60, ["Chicago", "25-or-6-to-4"]),
    # Test that commas are removed
    (1980, 13, ["The-Spinners", "Working-My-Way-Back-to-You/Forgive-Me-Girl"]),
    # Test that plus signs are removed
    (2020, 22, ["Dan-Shay-and-Justin-Bieber", "10000-Hours"]),
    # Test that if there is " – ", it is removed
    (2020, 34, ["Jawsh-685-and-Jason-Derulo", "Savage-Love-Laxed-Siren-Beat"]),
    # Test that periods are removed
    (2020, 98, ["HER", "Slide"]),
    # Test that anything after the word "featuring" is removed
    (2020, 89, ["Rod-Wave", "Rags2Riches"]),
]


@pytest.mark.parametrize("year,element,answer", test_cases_get_table)
def test_get_table(year, element, answer):
    """
    Test that the get_table function outputs match the series of test
    cases written above

    Args:
        year: the year that is being tested
        element: the element of the list that is being tested
        answer: the answer (written in test_cases_get_table) that the
        function should output
    """
    function_answer = get_table(year)[element]
    assert function_answer == answer


# Define a set of test cases for lyrics function -- these numbers were found by
# going to the genius lyrics website and counting the number of words per song
test_cases_genius_lyrics = [
    # Test a case where no bad words exist in a song
    (
        "https://genius.com/The-Weeknd-Blinding-Lights-lyrics",
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
        },
    ),
    # Test WAP by Cardi B
    (
        "https://genius.com/Cardi-B-WAP-lyrics",
        {
            "fuck": 2,
            "shit": 0,
            "ass": 0,
            "bitch": 0,
            "cunt": 0,
            "dick": 1,
            "sex": 0,
            "slut": 0,
            "pussy": 16,
            "crap": 0,
            "hell": 0,
            "cock": 0,
            "penis": 0,
            "bussy": 0,
            "motherfucker": 0,
            "hoe": 0,
            "whore": 0,
            "munch": 0,
        },
    ),
    # Test Good as Hell by Lizzo
    (
        "https://genius.com/Lizzo-Good-as-Hell-lyrics",
        {
            "fuck": 0,
            "shit": 2,
            "ass": 3,
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
        },
    ),
]


@pytest.mark.parametrize("song_link,answer", test_cases_genius_lyrics)
def test_genius_lyrics(song_link, answer):
    """
    This function tests the lyrics function. It takes in a URL and the desired answer
    and compares it to the answer the function outputs.

    Args:
        song_link: a URL of the website that will be scraped
        answer: a dictionary that is the right output the function should have
    """
    function_answer = lyrics(song_link)
    assert function_answer == answer
