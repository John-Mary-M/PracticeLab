"""cs50p 5/11/2023 problemset 7 um.py
"""
import re

# import sys


def main():
    """Entry point"""
    print(count(input("Text: ")))


def count(s):
    """expects a line of text as input as a str and returns, as an int,
    the number of times that “um” appears in that text, case-insensitively,
    as a word unto itself, not as a substring of some other word.
    For instance, given text like hello, um, world, the function should
    return 1. Given text like yummy, though, the function should return 0."""

    match = re.findall(r"\bum\b", s, re.IGNORECASE)
    # print(len(match))
    # if match:
    #     occurence = 0
    #     for match in s:
    #         occurence = +1
    #     return occurence
    return len(match)


if __name__ == "__main__":
    main()
