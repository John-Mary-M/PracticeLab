"""cs50 final project experiement"""
import csv
from argparse import ArgumentParser


def main():
    """Entry point"""
    args = parse_arguments()

    if args.file:
        read_from_file(args.file)
    else:
        shopping_list, prices = get_input()
        print(type(shopping_list))
        print(shopping_list)

        # Call store_input with the appropriate arguments
        items, quantities, prices = parse_shopping_list(shopping_list)
        subtotals = calculate_subtotals(quantities, prices)
        store_input(items, quantities, prices, subtotals)

        # Call calculate_total_cost and print the result
        total_cost = calculate_total_cost(quantities, prices)
        print(f"Total Cost: {total_cost}")


def parse_arguments():
    """Parse command-line arguments"""
    parser = ArgumentParser(
        description="Manage shopping lists and calculate total cost."
    )
    parser.add_argument("--file", "-f", help="Specify the CSV file to read")
    args = parser.parse_args()
    return args


def get_input():
    """Gets items, quantities, and prices from user"""
    parser = ArgumentParser(description="gets user items, quantities, and prices from")
    parser.add_argument(
        "pairs",
        nargs="+",
        help="Pairs of item, quantity, and price (e.g., 'banana 30 0.5')",
    )
    args = parser.parse_args()

    if not args.pairs:
        return "Error No items provided"

    input_string = " ".join(args.pairs)
    items = input_string.split(" ")

    # Validate that the number of items is a multiple of 3
    if len(items) % 3 != 0:
        return "Error: Each item should have a corresponding quantity and price."
    else:
        quantities = items[1::3]
        prices = items[2::3]

        input_strings = []
        for item, quantity, price in zip(items[::3], quantities, prices):
            input_strings.append(f"Item: {item}, Quantity: {quantity}, Price: {price}")

        return "\n".join(input_strings), prices


def store_input(items, quantities, prices, subtotals):
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
        for item, quantity, price, subtotals in zip(items, quantities, prices):
            writer.writerow([item, quantity, price, subtotals])


def parse_shopping_list(shopping_list):
    """Parses the formatted shopping list string into items, quantities, and prices"""
    # Implement the parsing logic here based on the formatting of shopping_list
    # For now, assuming shopping_list is formatted like 'Item: item1, Quantity: quantity1, Price: price1\nItem: item2, Quantity: quantity2, Price: price2'
    items = []
    quantities = []
    prices = []
    lines = shopping_list.split("\n")
    for line in lines:
        parts = line.split(", ")
        item = parts[0].split(": ")[1]
        quantity = parts[1].split(": ")[1]
        price = parts[2].split(": ")[1]
        items.append(item)
        quantities.append(quantity)
        prices.append(price)
    return items, quantities, prices


def calculate_total_cost(quantities, prices):
    """Calculates the total cost based on quantities and prices"""
    total_cost = sum(
        float(quantity) * float(price) for quantity, price in zip(quantities, prices)
    )
    return total_cost


def calculate_subtotals(quantities, prices):
    """Calculates subtotals based on quantities and prices"""
    subtotals = [
        float(quantity) * float(price) for quantity, price in zip(quantities, prices)
    ]
    return subtotals


def read_from_file(file_name):
    """Reads data from a CSV file and prints it"""
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)

            # Print the headers
            headers = next(reader)
            print(", ".join(headers))

            # Print the remaining rows
            for row in reader:
                print(", ".join(row))
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")


if __name__ == "__main__":
    main()
