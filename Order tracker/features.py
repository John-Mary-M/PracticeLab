"""this module defines the features of the oder tracking app"""
import json
import cmd
import datetime

class Base(cmd.Cmd):
    """the line oriented interpreter"""
    prompt = ':) '
    orders = []
    updated_time = ""
    
    def do_create_order(self, arg):
        """Creates an order
        But doesnt save.
        To save you still have to use the 
        save command
        """
        name = input('Enter Order/ Client name: ')
        
        while True:
            con = input('Has this order been confirmed? ')
            if con.lower() == 'Yes'.lower():
                con = "confirmed"
                break
            elif con.lower() == 'No'.lower():
                con = "Pending"
                break
            else:
                print("Invalid Input")
        time_created = datetime.datetime.now()
        time_created = time_created.strftime('%d-%m-%Y %H:%M:%S')
        estimated_cost = float(input('How much will this order cost to fullfil? '))
        
        order = {
            'name': name,
            'time_created': time_created,
            'status': con,
            'estimated_cost': estimated_cost,
            'time_updated': Base.updated_time
        }
        Base.orders.append(order)
        print("order created successfully\nDont forget to save the data")
        
    def do_show_order(self, arg):
        """Shows all orders, that are currently loaded
        in the base class
        """
        self.do_save_data
        if not Base.orders:
            print("No orders vailable.")
            return
        for order in Base.orders:
            if 'estimated_cost' not in order:
                order['estimated_cost'] = 'unknown'
            if 'time_updated' not in order:
                order['time_updated'] = 'Not yet'
            else:
                print(f"Name: {order['name']} Time created: {order['time_created']}  Order Status: {order['status']} Order Cost: {order.get('estimated_cost', 'unknown')} Updated: {order['time_updated']}")
            print()
            
            
    def do_search_order(self, arg):
        """Searches for an order"""
        self.arg = arg
        found_order = []
        for order in Base.orders:
            if arg.lower() in order['name'].lower():
                found_order.append(order)
        if found_order:
            print("Found order:")
            for found in found_order:
                print(f"Name: {found['name']} Time created: {found['time_created']} Order Status: {found['status']} Order Cost: {found.get('estimated_cost', 'unknown')} Updated: {found.get('time_updated', ' ')}")
                print()
        else:
            print("No match found.")
        
    def do_EOF(self, arg):
        return True
        print()
    
    def do_save_data(self, arg):
        """Saves data as a json string"""
        data = json.dumps(Base.orders)
        with open('data.json', 'w') as file:
            file.write(data)
        print("Data saved successfully!")
        print()
        
    def do_load_data(self):
        """Loads data from a JSON string into the base class
        But doesnt display data
        To display the data you still have to use the show
        command
        """
        try:
            with open('data.json', 'r') as f:
                data = f.read()
                Base.orders = json.loads(data)
            print("Data loaded successfully!")
        except FileNotFoundError:
            print("No data file found.")
            
    def do_update_order(self, arg):
        """Updates an element of an order or an entire order
        To update anything, first the data has to be loaded into the
        base class with the load data command
        """
        self.do_load_data()
        self.do_show_order(None)
        order_index = int(input("Enter the order number you want to update: "))
        if order_index < 0 or order_index >= len(Base.orders):
            print("Invalid order number.")
            return
        order = Base.orders[order_index]
        
        feild = input("Enter the feild to update (name, time_created, status, estimated_cost, time_updated): ")
        if feild  not in order:
            print("Invalid field.")
            return
        
        new_value = input(f"Enter new value for {feild}: ")
        if feild == 'estimated_cost':
            try:
                new_value = float(new_value)
            except ValueError:
                print("Invalid value for estimated_cost. Please enter a number.")
                return
            
        order[feild] = new_value
        order['time_updated'] = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        self.do_save_data(None)
        print("Order updated successfully!")