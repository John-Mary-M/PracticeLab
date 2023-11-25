"""cs50p final project 13/11/2023
    pos.py is a point of sale software that allows user to
    input a list of items bought a long with their prices and
    quantities. In return pos calculates a fixed VAT,
    puts a time/ date stamp, keeps a copy of the record and
    prints back a receipt to the user
"""


class Pos:
    def __init__(self, items: list, prices: int, quantities: int):
        self._items = items
        self._prices = prices
        self._quantities = quantities

    @property
    def get_items(self):
        """
        gets items
        """
        return self._items

    @get_items.setter
    def set_items(self, new_items: list):
        """Sets items to a list"""
        updated_item_list = self._items.append(new_items)
        return updated_item_list

    @property
    def get_prices(self):
        """gets item's price"""
        return self._prices

    @get_prices.setter
    def set_price(self, amount):
        """sets item's price"""
        self._price = amount
        return self._price

    @property
    def get_quantities(self):
        """gets item qnty"""
        return self._quantities

    # def __str__(self):
    #     return
