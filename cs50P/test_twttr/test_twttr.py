"""cs50p 2/10/2023 problemset 5"""
from twttr import shorten


def test_vowel_removal():
    assert shorten("Vowelia") == "Vwl"


def test_lowercase_vowel_removal():
    assert shorten("Vowelia") == "Vwl"


def test_uppercase_vowel_removal():
    assert shorten("VOwElIa") == "Vwl"
