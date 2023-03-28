"""
Create tests for the get_table function and implement them
in the test_get_table function
"""
import pytest
from get_data import get_table

# Define sets of test cases

test_cases_get_table = [
    # Test that the 98th element of the 1990's list
    # is ['Mentirosa', 'Mellow Man Ace']
    (1990, 98, ["Mentirosa", "Mellow Man Ace"]),
    # Test that the function removed extra forward slashes
    (1990, 59, ["Can't Stop", "After 7"]),
    # Test that the function removed extra quotation marks
    (1990, 79, ["Romeo", "Dino"]),
    # Test that the 16th element of the 2000's list
    # is ["Music", "Madonna"]
    (2000, 16, ["Music", "Madonna"]),
    # Test that the 26th element of the 2000's list
    # is ["It's Gonna Be Me", 'N Sync]
    (2000, 26, ["It's Gonna Be Me", "'N Sync"]),
    # Test that special letters like the squiggly Spanish n
    # show up
    (2020, 43, ["Señorita", "Shawn Mendes and Camila Cabello"]),
    # Test that parentheses show up properly and that ampersands show up
    (
        1960,
        74,
        [
            "A Rockin' Good Way (To Mess Around and Fall in Love)",
            "Dinah Washington & Brook Benton",
        ],
    ),
    # Test that dashes show up
    (1960, 83, ["Happy-Go-Lucky Me", "Paul Evans"]),
    # Test the 26th element of the 1970s list
    (1970, 25, ["Which Way You Goin' Billy?", "The Poppy Family"]),
    # Test the 34th element of the 1970s list
    (1970, 33, ["Instant Karma!", "John Lennon"]),
    # Test the 61st element of the 1970s list
    (1970, 60, ["25 or 6 to 4", "Chicago"]),
    # Testing that the 14th element of the 1980s list has the forward
    # slash show up
    (1980, 13, ["Working My Way Back to You/Forgive Me, Girl", "The Spinners"]),
    # Testing the 23rd element of the 2020s list
    (2020, 22, ["10,000 Hours", "Dan + Shay and Justin Bieber"]),
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
