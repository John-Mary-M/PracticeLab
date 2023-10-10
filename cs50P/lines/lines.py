"""CS50p Problemset 6 File I/O, Lines of Code 10/10/2023"""

import sys


def main():
    """Entry point"""
    try:
        file = sys.argv[1]
        lines = count_lines(file)
        print(lines)
    except IndexError:
        sys.exit("Too few command-line arguments")


def count_lines(file):
    """Takes a file specifies in the commandline arguement
    counts lines in the file
    excluding comments and blanklines
    """
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not (sys.argv[1].endswith(".py")):
        sys.exit("Not a Python file")
    else:
        try:
            with open(file, "r") as file:
                lines = file.readlines()
                count = 0
                for line in lines:
                    # Remove leading and trailing whitespaces
                    line = line.strip()
                    # skip empty lines
                    if not line:
                        continue
                    # skip lines starting with #
                    if line.startswith("#"):
                        continue
                    count += 1
                return count
        except FileNotFoundError:
            sys.exit("File does not exist")

if __name__ == "__main__":
    main()
