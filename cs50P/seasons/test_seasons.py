"""pytests for seasons"""
import pytest
from datetime import date
from seasons import get_date, tot_minutes

def main():
    """Entry point"""
    test_get_valid_date()
    test_get_invalid_date()
    test_tot_minutes()

def test_get_valid_date():
    """tests user input"""
    assert get_date("1999-01-01") == "1999-01-01"

def test_get_invalid_date():
    """checks user input for invalid date"""
    with pytest.raises(SystemExit):
        get_date("1999/01/01")

def test_tot_minutes():
    """Test conversion of days to minutes"""
    assert tot_minutes(10) == 10 * 24 * 60  # Days to Minutes conversion

if __name__ == "__minute__":
    main()
