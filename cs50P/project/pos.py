"""Experimenting with argparse"""
import argparse
import csv


def main():
    """Entry Point"""
    shopping_list = get_input()
    store_input(shopping_list)
    display = print_output(shopping_list)
    print(display)


def get_input():
    """gets user shoping list"""
    parser = argparse.ArgumentParser(
        description="Multiple items and prices and quantities"
    )
    parser.add_argument(
        "item",
        nargs="+",
        help="Items to buy, the quantity and price for each e.g banana 3 780",
    )
    # parser.add_argument('qnty', type=int, help='Qunatity of each item to buy')
    # parser.add_argument('price', type=int, help='Cost per item to buy')
    args = parser.parse_args()

    if not args:
        return "Error No items provided"

    items = args.item
    shopping_list = []

    for i in range(0, len(items), 3):
        item = items[i]
        quantity = int(items[i + 1])
        price = int(items[i + 2])
        sub_total = quantity * price
        shopping_list.append([item, quantity, price, sub_total])

    return shopping_list

def print_output(shopping_list):
    """Prints the shopping list"""
    total = 0
    # print('Item \t Qnty \t Price \t Subtotal')
    for item in shopping_list:
        print(f"{item[0]} \t {item[1]} \t {item[2]} \t {item[3]}")
        # print(f"Quantity: {item[1]}")
        # print(f"Price: {item[2]}")
        # print(f"Subtotal: {item[3]}")
        print("----------------------------------------------")
        total += item[3]
    return f"Total: {total}"

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
