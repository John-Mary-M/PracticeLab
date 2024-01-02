"""cs50p problemset 8 10/11/2023
     program that prompts the user for their date of birth in YYYY-MM-DD
     format and then rints how old they are in minutes, rounded to the
     nearest integer, using English words instead of numerals,  without
     any and between words. Since a user might not know the time at which
     they were born, assume, for simplicity, that the user was born at midnight
     (i.e., 00:00:00) on that date. And assume that the current time is also
     midnight. In other words, even if the user runs the program at noon,
     assume that it’s actually midnight, on the same date
"""
import sys
from datetime import date
import re
import inflect

p = inflect.engine()


def main():
    """Entry Point"""
    birth_day = input("Date of Birth ")
    birth_day = get_date(birth_day)
    year, month, day = birth_day.split("-")
    date_of_birth = date(int(year), int(month), int(day))

    current_date = date.today()
    print(current_date)

    # difference between the dates in days
    age = current_date - date_of_birth
    age = age.days

    # converting the days to minutes
    minutes_on_earth = tot_minutes(age)

    # converting minutes to words
    display = p.number_to_words(minutes_on_earth, andword="")
    print(display.capitalize() + "minutes")


def get_date(dob):
    """gets users date of birth"""
    if re.search(r"^\d{4}-\d{2}-\d{2}$", dob):
        return dob
    else:
        sys.exit("Invalid date")


def tot_minutes(age):
    """converts days to minutes"""
    minutes = age * 24 * 60
    return minutes


if __name__ == "__main__":
    main()
