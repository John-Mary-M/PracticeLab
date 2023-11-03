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
    if match := re.search(r'(https?://[www]?\.?)(youtube\.)(\w*?"?\/embed)(\/?\w*"?)', s, re.MULTILINE):
        pre, e, f = match.group(1), match.group(2), match.group(4)
        # f = re.sub(r'/', '', f)
        url = f"{pre}{e}{f}".replace('"', "")
        url = re.sub(r'youtube.', 'youtu.be', url)
        return url


if __name__ == "__main__":
    main()
# /(\w+:\/\/\w*\.\w*\.\w*\/\w*\/\w*")
