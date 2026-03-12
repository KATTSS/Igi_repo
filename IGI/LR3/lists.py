"""LR3/igi
Input module
Version: 1.0
Author: Ekaterina Butkevich
Group: 453501
Date: 12.03.2026
"""
import random

def get_amount_pos_bigger_constant(compare_constant, list_):
    """Returns amount of positive elements > C."""
    count=0

    for el in list_:
        if el>compare_constant and el>0:
            count+=1

    return count

def find_max_pos(list_):
    """Returns a position of the biggest list element."""
    
    max_elem = list_[0]
    max_elem_pos=0

    for i, el in enumerate(list_):
        if el>max_elem:
            max_elem=el
            max_elem_pos=i
    
    return max_elem_pos

def multiply_from_pos(list_, pos):
    """Returns multiplication of all list elements after some position."""

    if pos+1 > len(list_) or pos<0:
        return 0
    
    res=list_[pos]

    for i in range(pos+1, len(list_)):
        res*=list_[i]
    return res

def autogenerate_list(size):
    """Returns a sized generated list."""
    return list(generator(size))

def generator(n):
    """Generator for sequense."""
    for i in range(n):
        yield random.randint(-i, i)
