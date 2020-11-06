# import waiter child class
from waiter_class import Waiter
# import counter class, so we can display there order nicely
from collections import Counter

# define function that displays the user order nicely
def user_order(a_list):
    for key, val in Counter(a_list).items():
        print(f"{val} {key}")

if __name__ == "__main__":
    # make an object of waiter
    Waiter_1 = Waiter()

    # display menu
    Waiter_1.display_menu()

    # get what the customers ordered
    customer_order = Waiter_1.ordering()

    # print the order and the price
    print(f'So your order is:\n{user_order(customer_order)}\nAnd that will come to £{Waiter_1.total_price(customer_order)}')