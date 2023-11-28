"""tests the functionality of the shoppers App"""

import csv
import os
import pytest
from tabulate import tabulate
from project import get_input, print_output, store_input


def test_get_input_empty(monkeypatch):
    """
    Test get_input function.

    """
    monkeypatch.setattr("sys.argv", ["project.py"])
    assert get_input() == "Invalid Input"


def test_get_input_valid(monkeypatch):
    """Test get_input function for valid input"""

    # Set the value of sys.argv to simulate command-line arguments
    monkeypatch.setattr("sys.argv", ["project.py", "banana", "3", "780"])

    result = get_input()
    assert result == [["banana", 3, 780, 2340]]


def test_print_output(capsys):
    """
    Test print_output function.
    Ensure that the print_output function correctly formats and prints the shopping list.
    """
    shopping_list = [
        ["banana", 3, 780, 2340],
        ["apple", 2, 100, 200],
        ["korg", 1, 234, 234],
    ]

    # Format the expected output using tabulate with "plain" table format
    expected_output = tabulate(
        shopping_list,
        headers=["Item", "Quantity", "Price", "Subtotal"],
        tablefmt="plain",
    )

    print_output(shopping_list)
    captured = capsys.readouterr()

    # Format the captured output using the same "plain" table format
    captured_output = tabulate(
        shopping_list,
        headers=["Item", "Quantity", "Price", "Subtotal"],
        tablefmt="plain",
    )

    # Print captured and expected output for troubleshooting
    print("Captured Output:")
    print(captured_output.strip())
    print("Expected Output:")
    print(expected_output.strip())

    # Assert with ignoring leading and trailing whitespaces
    assert captured_output.strip() == expected_output.strip()


@pytest.fixture
def cleanup_csv_file():
    """Ensure the CSV file is deleted before each test"""
    csv_file = "user_input.csv"
    if os.path.exists(csv_file):
        os.remove(csv_file)


def test_store_input_existing_file(cleanup_csv_file):
    """Test store_input function with an existing CSV file."""
    # Create an existing CSV file with headers
    csv_file = "user_input.csv"
    headers = ["Item", "Quantity", "Price", "Subtotal"]
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(headers)
    # Input list to be stored
    input_list = [["banana", 3, 780, 2340], ["apple", 2, 100, 200]]

    # Call the store_input function
    store_input(input_list)

    # Verify the content of the CSV file
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert rows == [headers, ["banana", "3", "780", "2340"], ["apple", "2", "100", "200"]]

def test_store_input_new_file(cleanup_csv_file):
    """Test store_input function with a new CSV file."""
    # Input list to be stored
    input_list = [["banana", 3, 780, 2340], ["apple", 2, 100, 200]]

    # Call the store_input function
    store_input(input_list)

    # Verify the content of the CSV file
    csv_file = "user_input.csv"
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert rows == [["Item", "Quantity", "Price", "Subtotal"], ["banana", "3", "780", "2340"], ["apple", "2", "100", "200"]]

if __name__ == "__main__":
    pytest.main()
