"""LR3/igi
Input module
Version: 1.0
Author: Ekaterina Butkevich
Group: 453501
Date: 10.03.2026
"""

def input_decorator(input_type):
    """A decorator for different type input"""
    def decorator(func):
        def wrapper():
            print(f"Enter a {input_type}:")
            return func()
        return wrapper
    return decorator


@input_decorator("integer")
def get_user_int():
    """Integer input handler: returns int value from keyboard"""
    while True:
        try:
            return int(input())
        except ValueError:
            print("Error. Try again")


@input_decorator("float")
def get_user_float():
    """Float input handler: returns float value from keyboard"""
    while True:
        try:
            return float(input())
        except ValueError:
            print("Error. Try again")
