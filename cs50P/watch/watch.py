"""cs50p Problemset 7 regex 2/11/2023 watch.py
    A program that searches through iframe elements for embeded 
    youtube video links, extracts and returns the orignal URL and 
    in a case where there is no youtube link it returns none"""

import re


def main():
    """Entry point"""
    print(parse(input("HTML: ")))


def parse(s):
    """extracts youtube url from an iframe element"""
    if re.search(r'^<iframe.*<\/iframe>$', s):
        url_match = re.search(
            r'(http)(s)*:\/\/(www\.)*(youtube\.com\/)embed\/(\w*)', s, re.MULTILINE
                              )
        if url_match:
            url_prt = url_match.groups()
            return "https://youtu.be/" + url_prt[4]
        return None

if __name__ == "__main__":
    main()
# /(\w+:\/\/\w*\.\w*\.\w*\/\w*\/\w*")
