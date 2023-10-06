"""cs50p 6/10/2023 test for fuel.py"""
from fuel import convert
from fuel import gauge

# Testing the gauge function
def test_gauge_F():
    '''tests full gauge'''
    assert gauge(100) == 'F'
    assert gauge(99) == 'F'
    
def test_gauge_E():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    
def test_gauge_percentage():
    assert gauge(50) == "50%"
    assert gauge(75.5) == "76%"

# Test cases for the 'convert' function
def test_convert_valid_fraction():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    
def test_convert_invalid_fraction():
    # Test for an invalid fraction (denominator is 0)
    try:
        convert("5/0")
    except ValueError:
        assert ValueError is ValueError
        
def test_convert_percentage():
    assert convert("25/25") == 100
    assert convert("0/100") == 0