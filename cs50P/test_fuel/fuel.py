"""cs50 problemset 5 reimplementing the fuel gauge program
    6/10/2023
"""


def main():
    """Entry point"""
    while True:
        try:
            fraction_str = input("Faction: ")
            percentage = convert(fraction_str)
            fuel_level = gauge(percentage)
            print(f'{fuel_level}')
            break
        except ValueError:
            pass
        # break
def convert(fraction):
    """
    expects a str in X/Y format as input, wherein each of X and Y is
    an integer, and returns that fraction as a percentage rounded to
    the nearest int between 0 and 100, inclusive. If X and/or Y is not
    an integer, or if X is greater than Y, then convert should raise a
    ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
    """
    try:
        numerator, denominator = map(int, fraction.split("/"))
        if denominator == 0 or numerator > denominator:
            raise ValueError
        return min(max(round((numerator/denominator)* 100), 0), 100)
        # percentage = round((numerator / denominator) * 100)
        # if percentage < 0:
        #     return 0
        # elif percentage > 100:
        #     return 100
        # else:
        #     return percentage
    except (ValueError, ZeroDivisionError):
        raise


def gauge(percentage):
    """
    gauge expects an int and returns a str that is:
    "E" if that int is less than or equal to 1,
    "F" if that int is greater than or equal to 99,
    and "Z%" otherwise, wherein Z is that same int.
    """
    match percentage:
        case 100 | 99:
            return "F"
        case 0|1:
            return "E"
        case _:
            # return str(percentage) + '%'
            return f'{percentage:.0f}%'

if __name__ == "__main__":
    main()
