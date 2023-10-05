"""cs50p Problemset 5 4/10/2023 tests for the vanity plates program"""
from plates import is_valid


def test_two_letters_begining():
    """tests for presence of at leat 2 letters at the start"""
    assert is_valid("AA222") is True


def test_numbers_end_only():
    """tests for numbers presence at the end"""
    assert is_valid("AAA222") is True


def test_numbers_in_middle_only():
    """tests for presence of numbers in the middle of the plate
    which should yeild false/ invalid plate
    """
    assert is_valid("cs50P") is False


def test_short_length_plate():
    """Tests for a short plate"""
    assert is_valid("H") is False


def test_longer_plates():
    """tests for long plates"""
    assert is_valid("CsPcsP500") is False

def test_begins_with_digit():
    """test for plates begining with digits instead of alphabet characters"""
    assert is_valid("55CSX") is False

def test_invalid_plate_starts_with_zero():
    assert is_valid("AB0123") is False

def test_invalid_plate_does_not_start_with_letters():
    assert is_valid("123ABC") is False

def test_invalid_plate_contains_punctuation():
    assert is_valid("AB.CD") is False
    assert is_valid("A,BCD") is False
    assert is_valid("AB?CD") is False
    assert is_valid("AB CD") is False
    assert is_valid("A!BCD") is False