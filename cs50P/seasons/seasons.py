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
import inflect


class DateUtils:
    """Has functionalities that enable minute counting from birt till date"""

    def __init__(self, birth_date):
        self.birth_date = birth_date

    def calculate_minutes_lived(self):
        """counts the total minutes lived till date"""
        current_date = date.today()
        year_difference = current_date.year - self.birth_date.year

        total_days = year_difference * 365  # Approximation for simplicity

        for year in range(self.birth_date.year, current_date.year):
            if self.is_leap_year(year):
                total_days += 1  # Add an extra day for leap years

        total_minutes = total_days * 24 * 60  # Convert days to minutes

        return total_minutes

    @staticmethod
    def is_leap_year(year):
        """checks for leap year"""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


class WordsConverter:
    """Converts minutes from int to words"""

    @staticmethod
    def convert_to_words(minutes):
        p = inflect.engine()
        return p.number_to_words(int(round(minutes)))


def get_date():
    """Gets date of birth from the user"""
    try:
        birth_day_str = input("Date of Birth: ")
        year, month, day = map(int, birth_day_str.split("-"))
        return date(year, month, day)
    except ValueError:
        sys.exit("Ivalid date")


def main():
    """Entry Point"""
    birthday = get_date()
    if birthday:
        date_util = DateUtils(birthday)
        minutes_lived = date_util.calculate_minutes_lived()
        minutes_in_words = WordsConverter.convert_to_words(minutes_lived)
        print(f"{minutes_in_words}")


if __name__ == "__main__":
    main()
