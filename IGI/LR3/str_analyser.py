"""LR3/igi
String handler module
Version: 1.0
Author: Ekaterina Butkevich
Group: 453501
Date: 11.03.2026
"""

def find_lowercase_count(s):
    """Returns amount of lowercase symbols in string."""
    count=0
    for symbol in s:
        if symbol.islower():
            count += 1
    return count

def find_digit_count(s):
    """Returns amount of digits in string."""
    count = 0
    for symbol in s:
        if symbol.isdigit():
            count += 1
    return count