"""cs50p Final project started on 18/11/2023
    Project title: Shopper's App
    Writen by: Mukisa John Mary
    Language: English
    Purpose of the App: To give the shopper a quick view of their costs
    or estimates before they make them. Stores a csv record of these estimates
    for later revision.
"""
import argparse
import csv
from tabulate import tabulate


def main():
    """Entry Point"""
    shopping_list = get_input()
    store_input(shopping_list)
    display = print_output(shopping_list)
    print(display)


def get_input():
    """gets user shoping list"""
    try:
        parser = argparse.ArgumentParser(
            description="Multiple items and prices and quantities"
        )
        parser.add_argument(
            "item",
            nargs="+",
            help="Items to buy, the quantity and price for each e.g banana 3 780",
        )
        args = parser.parse_args()

        if not args.item:
            raise argparse.ArgumentError(None, "Error: No items provided")

        items = args.item
        shopping_list = []

        for i in range(0, len(items), 3):
            item = items[i]
            quantity = int(items[i + 1])
            price = int(items[i + 2])
            sub_total = quantity * price
            shopping_list.append([item, quantity, price, sub_total])

        return shopping_list
    except SystemExit:
        return "Invalid Input"


def print_output(shopping_list):
    """Prints the shopping list"""

    try:
        total = 0
        headers = ["Item", "Quantity", "Price", "Subtotal"]
        rows = [[item[0], item[1], item[2], item[3]] for item in shopping_list]

        print(tabulate(rows, headers=headers, tablefmt="pretty"))

        for item in shopping_list:
            total += item[3]

        return f"Total: {total}"
    except (SystemExit, IndexError):
        return "Invalid input formart"


def store_input(input_list):
    """Stores User Input in a csv file"""
    csv_file = "user_input.csv"

    # Check if the file exists, if not, create it and write header
    headers = ["Item", "Quantity", "Price", "Subtotal"]
    try:
        with open(csv_file, "x", newline="") as file:
            writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(headers)
    except FileExistsError:
        pass  # File already exists, no need to write header

    # Append user input to the CSV file
    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        for item in input_list:
            writer.writerow(item)


if __name__ == "__main__":
    main()
