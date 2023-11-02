"""cs50p Problemset 7 regex 2/11/2023 watch.py
    A program that looks through embeded youtube videos,
    extracts and returns the orignal URL and in a case where 
    there is no youtube link it returns none"""
    
import re

def main():
    """Entry point"""
    print(parse(input("HTML: ")))


def parse(s):
    """extracts youtube url from an iframe element"""
    if match := re.search(r'(\w*:\/\/\w*\.\w*\.\w*)(\/\w*\/)(\w*)', s, re.MULTILINE):
        link, a = match.group(1), match.group(3)
        return f"{link + a}"

if __name__ == "__main__":
    main()
# /(\w+:\/\/\w*\.\w*\.\w*\/\w*\/\w*")