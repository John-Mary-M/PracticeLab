"""cs50p 2/10/2023 problemset 5"""
from twttr import shorten


def test_vowel_removal():
    assert shorten("Vowelia") == "Vwl"


def test_lowercase_vowel_removal():
    assert shorten("Vowelia") == "Vwl"


def test_uppercase_vowel_removal():
    assert shorten("VOwElIa") == "Vwl"

def test_numbers():
    assert shorten('123') == '123'
    
def test_punctuation():
    assert shorten("Vowels, and ?") == "Vwls, nd ?"

def test_numbers_as_args():
    try:
        shorten(123)
    except TypeError:
        pass
