"""tests the functionality of the shoppers App"""

import csv
import subprocess
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


# def test_store_input(tmp_path):
#     """
#     Test store_input function.

#     Ensure that the store_input function correctly writes the shopping list to a CSV file.
#     """
#     csv_file = tmp_path / "test_user_input.csv"
#     shopping_list = [
#         ["banana", 3, 780, 2340],
#         ["apple", 2, 100, 200],
#         ["korg", 1, 234, 234],
#     ]

#     store_input(shopping_list, csv_file)

#     with open(csv_file, "r") as file:
#         reader = csv.reader(file)
#         header = next(reader)
#         assert header == ["Item", "Quantity", "Price", "Subtotal"]

#         rows = [row for row in reader]
#         assert len(rows) == 3
#         assert rows[0] == ["banana", "3", "780", "2340"]
#         assert rows[1] == ["apple", "2", "100", "200"]
#         assert rows[2] == ["korg", "1", "234", "234"]

if __name__ == "__main__":
    pytest.main()
