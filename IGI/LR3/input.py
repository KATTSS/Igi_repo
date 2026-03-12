"""LR3/igi
Input module
Version: 1.0
Author: Ekaterina Butkevich
Group: 453501
Date: 10.03.2026
"""

def input_decorator(input_type):
    """A decorator for different type input."""
    def decorator(func):
        def wrapper():
            print(f"Enter a {input_type}:")
            return func()
        return wrapper
    return decorator


@input_decorator("integer")
def get_user_int():
    """Integer input handler: returns int value from keyboard."""
    while True:
        try:
            return int(input())
        except ValueError:
            print("Error. Try again")


@input_decorator("float")
def get_user_float():
    """Float input handler: returns float value from keyboard."""
    while True:
        try:
            return float(input())
        except ValueError:
            print("Error. Try again")

@input_decorator("string")
def get_user_string():
    """String input handler: returns string from keyboard."""
    while True:
        s = input()
        if s:
            return s
        print("Error. Try again")

def get_natural_num():
    """Returns only positive integer."""
    while True:
        x=get_user_int()
        if x>0:
            return x
        
def get_list(size):
    """Returns a sized list from a keyboard."""
    my_list=list()
    for i in range(size):
        new_el=get_user_float()
        my_list.append(new_el)
    return my_list

def get_yes_no():
    """Returns bool from user."""
    print("Press any key for YES or press ENTER for NO")
    x = input()
    if not x:
        return False
    return True

def get_menu_option(options_count):
    """Return a positive integer in range [1; options_count]."""
    x=-1

    while x<1 or x>options_count:
        x = get_user_int()
    return x