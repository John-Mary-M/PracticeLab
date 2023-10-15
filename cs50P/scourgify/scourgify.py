"""cs50p Problemset 6 11/10/2023 File I/O"""

import sys
import csv


def main():
    """Entry point of the program"""
    if check_cmd_args():
        read_csv(sys.argv[1])


def check_cmd_args():
    """Checks the presence of proper command-line arguments"""
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) == 3:
        try:
            with open(sys.argv[1], "r") as file:
                data = file.readline()
                if data:
                    return True
                else:
                    return False
        except (FileNotFoundError, IndexError):
            sys.exit("Could not read " + sys.argv[1])


def read_csv(file):
    """Reads the CSV file specified in sys.argv[1]
    and performs operations on the data"""
    with open(file, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        rows = list(csv_reader)  # read all rows into a list of dictionaries
        for row in rows:
            # Access the value of the "name" column
            value = row.pop("name")

            # Split the name into first and last based on comma and space
            first, last = value.split(" ", 1)
            row["first"] = last
            row["last"] = first.replace(',', '')


    # Write the modified rows to a new CSV file
    fieldnames = ["first", "last", "house"]
    with open(sys.argv[2], "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, quoting=csv.QUOTE_NONE, escapechar="\\")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
