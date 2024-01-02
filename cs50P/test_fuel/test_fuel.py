"""cs50p 6/10/2023 test for fuel.py"""
from fuel import convert, gauge
import pytest

# Testing the gauge function
def test_gauge_F():
    """tests full gauge"""
    assert gauge(100) == "F"
    assert gauge(99) == "F"


def test_gauge_E():
    """Testing E output"""
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_percentage():
    """Testing for other percentages"""
    assert gauge(50) == "50%"
    assert gauge(75.5) == "76%"


# Test cases for the 'convert' function
def test_convert_valid_fraction():
    """Testing for valid fractions"""
    assert convert("3/4") == 75
    assert convert("1/2") == 50


def test_convert_invalid_fraction():
    # Test for an invalid fraction (denominator is 0)
    with pytest.raises(ValueError):
        convert("xat/dog")


def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_convert_percentage():
    assert convert("25/25") == 100
    assert convert("0/100") == 0


def test_invalid_input():
    try:
        d = convert("cat/dog")
    except ValueError as v:
        print(v)
