"""cs50p pytest testing modules from ealier in the course
4/10/2023"""
from bank import value

def test_value_hello():
    assert value('hello, world') == 0
    
def test_value_hello_case_sensitive():
    assert value("HeLLo, WoRLd") == 0
    
def test_value_starting_with_h():
    assert value('help') == 20
    
def test_value_other_greeting():
    assert value('goodbye') == 100
    
def test_value_no_greeting():
    assert value('') == 100