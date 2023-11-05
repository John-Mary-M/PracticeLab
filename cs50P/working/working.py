"""cs50p 4/11/2023 problemset 7 working.py time converter function"""
import re

# import sys


def main():
    """Entry point"""
    print(convert(input("Hours: ")))


def convert(s):
    """coverts 12 hour clock time
    to 24 hour clock time"""
    match = re.search(r"^([0-9])(:?\d*\ \w*\ to\ )([0-9])(\ ?:?\d*\ \w*)", s)
    if not match:
        raise ValueError
    # check the arguements and prefix 0 or add 12
    if "AM" in match.group(2):
        hr_1 = "0" + match.group(1)
    elif "PM" in match.group(2):
        hr_1 = int(match.group(1)) + 12
    # check for PM and add 12
    if "PM" in match.group(4):
        hr_2 = int(match.group(3)) + 12
    elif "AM" in match.group(4):
        hr_2 = "0" + match.group(3)
    # format the result
    converted_time = f"{hr_1}{match.group(2)}{hr_2}{match.group(4)}"
    converted_time = re.sub(r"AM", "", converted_time)
    converted_time = re.sub(r"PM", "", converted_time)
    # conditionally remove the AM and PM and add the minutes
    if re.search(r"\w*", match.group(2)) and re.search(r"\w*", match.group(4)):
        converted_time = f"{hr_1}:00 to {hr_2}:00"

    return converted_time

if __name__ == "__main__":
    main()
