"""cs50p 10/10/2023 File I/O"""

import csv
import sys
from tabulate import tabulate


def main():
    """Entry point"""
    try:
        file = sys.argv[1]
        table = cmd_arguement(file)
        print(table)
    except IndexError:
        sys.exit("Too few command-line arguments")


def cmd_arguement(file):
    """checks for valid cmd line argument"""
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif not sys.argv[1].endswith(".csv"):
            sys.exit("Not a csv file")
        else:
            with open(file, "r") as file:
                csv_reader = csv.reader(file)
                header = next(csv_reader)
                # read the data into a list
                data = [row for row in csv_reader]
        return tabulate(data, header, tablefmt="grid")
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
