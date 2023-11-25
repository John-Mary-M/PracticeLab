"""cs50 final project experiement"""
import csv
from argparse import ArgumentParser


def main():
    """Entry point"""
    shoping_list = get_input()
    print(type(shoping_list))
    print(shoping_list)

    # Call store_input with the appropriate arguments
    items, quantities = parse_shopping_list(shoping_list)
    store_input(items, quantities)
    # store_input(item, quantit)


def get_input():
    """Gests items and qunatities from user"""
    parser = ArgumentParser(description="gets user items and quantities from")
    parser.add_argument(
        "pairs", nargs="+", help="Pairs of item and quantity (e.g., banana 30)"
    )
    args = parser.parse_args()

    # Validate that the number of pairs is even
    if len(args.pairs) % 2 != 0:
        return "Error: Each item should have a corresponding quantity."
    else:
        items = args.pairs[::2]
        quantities = args.pairs[1::2]

        input_strings = []
        for item, quantity in zip(items, quantities):
            input_strings.append(f"Item: {item}, Quantity: {quantity}")

        return "\n".join(input_strings)

        store_input(items, quantities)


def store_input(items, quantities):
    """Stores User Input in a csv file"""
    csv_file = "user_input.csv"

    # Check if the file exists, if not, create it and write header
    headers = ["Item", "Quantity"]
    try:
        with open(csv_file, "x", newline="") as file:
            writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(headers)
    except FileExistsError:
        pass  # File already exists, no need to write header

    # Append user input to the CSV file
    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        for item, quantity in zip(items, quantities):
            writer.writerow([f"{item}, {quantity}"])


def parse_shopping_list(shopping_list):
    """Parses the formatted shopping list string into items and quantities"""
    # Implement the parsing logic here based on the formatting of shopping_list
    # For now, assuming shopping_list is formatted like 'Item: item1, Quantity: quantity1\nItem: item2, Quantity: quantity2'
    items = []
    quantities = []
    lines = shopping_list.split("\n")
    for line in lines:
        parts = line.split(", ")
        item = parts[0].split(": ")[1]
        quantity = parts[1].split(": ")[1]
        items.append(item)
        quantities.append(quantity)
    return items, quantities


if __name__ == "__main__":
    main()
