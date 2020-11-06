# Creates parent class
class Menu:
    # Initialises the parent class with a full me menu inside as dictionary with prices
    def __init__(self):
        self.menu = {
            "ham & cheese panini": 3.99,
            "spaghetti bolognese": 7.99,
            "pepperoni pizza": 8.99,
            "cheesy omelette": 4.49,
            "steak sandwhich": 9.89,
            "ceasar salad": 4.49,
            "spicy chicken wrap": 6.79,
            "chips": 2.99,
            "pint of beer": 3.59,
            "bottle of wine": 14.99,
            "coca cola": 0.99
        }

    # define a function that displays_menu
    def display_menu(self):
        print("*"*11 + "MENU" + "*"*12)
        for key, val in self.menu.items():
            print(key + (" " * (20 - len(key))) + "- £" + str(val))

if __name__ == "__main__":
    menu = Menu()
    # testing printing menus functions
    print(menu.menu.items())
    for item in menu.menu.keys():
        print(item)
    print(menu.menu.values())

    menu.display_menu()
