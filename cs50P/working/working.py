"""cs50p 4/11/2023 problemset 7 working.py time converter function"""
import re


def main():
    """Entry point"""
    print(convert(input("Hours: ")))


def convert(s):
    """coverts 12 hour clock time
    to 24 hour clock time"""
    match = re.search(
        r"(\d+)(?::(\d+))?\s*(AM|PM)\s*to\s*(\d+)(?::(\d+))?\s*(AM|PM)", s
    )
    if not match:
        raise ValueError
    hr_1 = int(match.group(1))
    min_1 = int((match.group(2)) or "00")  # Use 0 if minutes are not provided
    if min_1 >= 60:
        raise ValueError
    am_pm_1 = match.group(3)
    hr_2 = int(match.group(4))
    min_2 = int((match.group(5)) or "00")
    if min_2 >= 60:
        raise ValueError
    am_pm_2 = match.group(6)

    # AM PM conversions
    if am_pm_1 == "PM" and hr_1 < 12:
        hr_1 += 12
    if am_pm_2 == "PM" and hr_2 < 12:
        hr_2 += 12
    converted_time = f"{hr_1:02}:{min_1:02} to {hr_2:02}:{min_2:02}"
    return converted_time


if __name__ == "__main__":
    main()
