# Shopper's App
#### Video Demo:  <URL HERE>
#### Description:
Shopper's App is a program/ software that gives any kind if shopper the ability to enter their shopping 
list in combination with all the estimated prices and quantites of items they will be buying and the app
calculates a subtotal for each item and also displays an over all total expense the shoper is looking at.

In additon the app displays the above information in a neat easy to read table format and also keeps
a copy of each entry the user makes in a csv file, giving the user the ability to later go back and import
the csv in their favorite spreadsheet software to do further tweaks or analysis of their expenditure.

## Implementation:
The app is implemented in python3 specifically the version i had at the time of its creation was python 3.10

I worte all the code in one file named `project.py` and the tests in `test_project.py` were i used pytest for 
the unit tests.

There are 3 major functions in the code on which the entire program is based namely `get_input`, `print_output`,
and `store_input`

- `get_input`: gets user shoping list with the help of argparse
- `print_output`: Formarts and Prints the user's shopping list with the help of tabulate 3rd party module
- `store_input`: Stores the user's shopping list in a csv file



### Dependencies:
- `argparse`
- `csv`
- `tabulate`

### Authors:
- [Mukisa John Mary](https://github.com/John-Mary-M)

#### TODO
- In the near future I will add a feature that lets the user view the csv file without having to first import it into
a spreadsheet software.
- In addition to this feature if possible i would like to make it possible for the user to edit and delete entries from 
the csv file for extra control.