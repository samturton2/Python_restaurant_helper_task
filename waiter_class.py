# import menu to create the waiter class as a child class of the menu
from menu_class import Menu

# Create class that asks what the user wants to order form its parent menu class
class Waiter(Menu):
    def __init__(self):
        super().__init__()

    # create a function that allows user to order
    def ordering(self):
        # Create an empty order list
        order_list = []
        ordering = True
        # loop to get the tables orders
        while ordering:
            # get the customers order
            cus_item = input("Please enter what you want.\n=>")

            # check if the order is on the menu
            if cus_item in self.menu.keys()