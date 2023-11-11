"""pytests for seasons"""

from datetime import date
import pytest
from seasons import DateUtils, WordsConverter, get_date


def main():
    test_calculate_minutes_lived()
    test_convert_to_words()
    test_invalid_date()
    # get_date(date_str)
    
def test_calculate_minutes_lived():
    """Test DateUtils class"""
    # Create a DateUtils instance for testing
    birth_date = date(1990, 1, 1)
    date_util = DateUtils(birth_date)

    # Calculate minutes lived
    minutes_lived = date_util.calculate_minutes_lived()

    # Test if the result is a positive number
    assert minutes_lived >= 0


def test_convert_to_words():
    """Test WordsConverter class"""
    # Test conversion for a specific number of minutes
    minutes = 123
    words = WordsConverter.convert_to_words(minutes)

    # Test the output format for a specific input
    assert words == "one hundred and twenty-three"


def test_invalid_date(capsys):
    """Test for invalid date input
        Capture the output when the function is called with 
        an invalid date"""
    with pytest.raises(SystemExit) as excinfo:
        seasons.get_date("Invalid Date String")
        assert excinfo.value.code == 'Invalid date\n'
        
   # Retrieve the captured output
    captured = capsys.readouterr()
    assert "Invalid date" in captured.out 

# def get_date(date_str):
#     """Helper function to get date from string for testing"""
#     try:
#         year, month, day = map(int, date_str.split("-"))
#         return date(year, month, day)
#     except ValueError:
#         return None

if __name__ == "__main__":
    main()
