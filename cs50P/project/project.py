"""cs50 final project experiement"""
import csv
from argparse import ArgumentParser


def main():
    """Entry point"""
    shopping_list, prices = get_input()
    print(type(shopping_list))
    print(shopping_list)

    # Call store_input with the appropriate arguments
    items, quantities, prices = parse_shopping_list(shopping_list)
    store_input(items, quantities, prices)
    
    # Call calculate_total_cost and print the result
    total_cost = calculate_total_cost(quantities, prices)
    print(f'Total Cost: {total_cost}')


def get_input():
    '''Gets items, quantities, and prices from user'''
    parser = ArgumentParser(description='gets user items, quantities, and prices from')
    parser.add_argument("pairs", nargs='+', help="Pairs of item, quantity, and price (e.g., banana 30 0.5)")
    args = parser.parse_args()

    # Validate that the number of pairs is a multiple of 3
    if len(args.pairs) % 3 != 0:
        return "Error: Each item should have a corresponding quantity and price."
    else:
        items = args.pairs[::3]
        quantities = args.pairs[1::3]
        prices = args.pairs[2::3]

        input_strings = []
        for item, quantity, price in zip(items, quantities, prices):
            input_strings.append(f'Item: {item}, Quantity: {quantity}, Price: {price}')

        return '\n'.join(input_strings), prices

        # store_input(items, quantities)


def store_input(items, quantities, prices):
    '''Stores User Input in a csv file'''
    csv_file = 'user_input.csv'

    # Check if the file exists, if not, create it and write header
    headers = ['Item', 'Quantity', 'Price']
    try:
        with open(csv_file, 'x', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(headers)
    except FileExistsError:
        pass  # File already exists, no need to write header

    # Append user input to the CSV file
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        for item, quantity, price in zip(items, quantities, prices):
            writer.writerow([item, quantity, price])


def parse_shopping_list(shopping_list):
    '''Parses the formatted shopping list string into items, quantities, and prices'''
    # Implement the parsing logic here based on the formatting of shopping_list
    # For now, assuming shopping_list is formatted like 'Item: item1, Quantity: quantity1, Price: price1\nItem: item2, Quantity: quantity2, Price: price2'
    items = []
    quantities = []
    prices = []
    lines = shopping_list.split('\n')
    for line in lines:
        parts = line.split(', ')
        item = parts[0].split(': ')[1]
        quantity = parts[1].split(': ')[1]
        price = parts[2].split(': ')[1]
        items.append(item)
        quantities.append(quantity)
        prices.append(price)
    return items, quantities, prices

def calculate_total_cost(quantities, prices):
    '''Calculates the total cost based on quantities and prices'''
    total_cost = sum(float(quantity) * float(price) for quantity, price in zip(quantities, prices))
    return total_cost

if __name__ == "__main__":
    main()
