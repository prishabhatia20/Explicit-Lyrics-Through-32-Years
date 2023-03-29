"""
Create tests for the get_table function and implement them
in the test_get_table function
"""
import pytest
from get_data import get_table

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
    (2020, 89, ["Rod-Wave", "Rags2Riches"])

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
