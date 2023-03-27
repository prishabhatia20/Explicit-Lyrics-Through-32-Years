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
]


@pytest.mark.parametrize("year,element,answer", test_cases_get_table)
def test_get_table(year, element, answer):
    function_answer = get_table(year)[element]
    assert function_answer == answer
