#!/usr/bin/python3
# 1st July 2023         Mastering OOP
"""This module defines objects used to keep track of inventory in a tech store"""
class Item:
        """Items, Their prices & quantities
        """
        pay_rate =0.8   # The pay rate after 20% discount
        def __init__(self, name: str, price: float, quantity=0):        # instace attributes
                """Constructor

                Args:
                    name (str): name of item
                    price (float): How much it costs
                    quantity (int, optional): Quantity sold. Defaults to 0.
                """
                # run checks aganist recived arguments
                assert price >= 0, f"Price {price} is not equal or greater than 0"
                assert quantity >= 0, f"Qnty {quantity} is not equal or greater than 0"
                
                # Assign to self Object
                self.name = name
                self.price = price
                self.quantity = quantity
        
        def calculate_total_price(self):
                """Calculates total prices for the items bought

                Returns:
                    total price of items sold_float/int_: total price.
                """
                return self.price * self.quantity
        
        def apply_discount(self):
                self.price = self.price * self.pay_rate
                
                
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
#print(Item.__dict__)    # All attributes for class level

#print(item1.__dict__)   # All attributes for instance level
