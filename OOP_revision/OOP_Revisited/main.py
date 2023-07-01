
# 1st July 2023         Mastering OOP
"""This module defines objects used to keep track of inventory in a tech store"""
import csv

class Item:
        """Items, Their prices & quantities
        """
        pay_rate =0.8   # The pay rate after 20% discount
        all = []        # Class attribute to access all instance attributes
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
                
                # actions to execute
                Item.all.append(self)   # add all objects to list as they are created
        
        def calculate_total_price(self):
                """Calculates total prices for the items bought

                Returns:
                    total price of items sold_float/int_: total price.
                """
                return self.price * self.quantity
        
        def apply_discount(self):
                self.price = self.price * self.pay_rate
         
        @classmethod    # decorator that converts method to class method      
        def instantiate_from_csv(cls):         # Class method: Can only be accessed from the class level only
                """Reads CSV file with our data

                Returns:
                    list of dictionaries: List containing all items in the csv
                """
                with open('items.csv', 'r') as f:
                       reader = csv.DictReader(f)
                       items = list(reader)
                
                # instantiate instances
                for item in items:
                        Item(
                                name=str(item.get('name')),
                                price=float(item.get('price')),
                                quantity=int(item.get('quantity')),
                        )
                #for item in items:      # print list of dictionaries
                        #print(item)
        
        @staticmethod
        def is_integer(num):
                """_summary_

                Args:
                    num (int/float): number to check

                Returns:
                   Bolean: _description_
                """
                # We ignore floats that are point zero
                # For example 5.0, 4.0
                if isinstance(num, float):
                        # ignore point zero
                        return num.is_integer
                elif isinstance(num, int):
                        return True
                else:
                        return False
                
                
        # another way to print a comprehesive list of all instances
        def __repr__(self):     # magice method similar to __str__
                return f"Item('{self.name}', {self.price}, {self.quantity})"
        
 
    
Item.instantiate_from_csv()

# to use the method above to acces the list of items
print(Item.all)

#for object in Item.all:         # printint the list of all instances/ objects
        #print(object.name)
        


#print(Item.__dict__)    # All attributes for class level

#print(item1.__dict__)   # All attributes for instance level
