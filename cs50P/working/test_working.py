"""pytests for working.py"""
from _pytest.junitxml import pytest
from pytest import raises
from working import convert


def main():
    test_day_time_1()
    test_day_time_2()
    test_night_time_1()
    test_night_time_2()


def test_day_time_1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_day_time_2():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_night_time_1():
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"


def test_night_time_2():
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"


def test_time_with_minutes():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_invalid_input():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
        convert("9 AM - 5 PM")
        convert("09:00 AM - 17:00 PM")


if __name__ == "__main__":
    main()
