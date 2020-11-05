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

        # loop to get the tables orders
        while True:
            # get the customers order
            cust_item = input("Please enter what you want.\n=>")

            # check if the order is on the menu
            if cust_item in self.menu.keys():
                order_list.append(cust_item) # If on the menu
            else:
                print("We dont have that item on the menu")

            # ask if the customer wants anything else
            more = input("Anything else? ")
            if more[0].lower() == "n":
                break

        return order_list

    def total_price(self, order_list):
        # work out the total price of what they ordered
        price = 0 # place holder for price
        for item in order_list:
            price += self.menu[item]
        return price