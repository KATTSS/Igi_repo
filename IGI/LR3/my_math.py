"""LR3/igi
Math module
Version: 1.0
Author: Ekaterina Butkevich
Group: 453501
Date: 10.03.2026
"""
from math import cos, pi

def row_calcilator(x=0, eps=0.01):
    """Calculates cos(x) using power series"""

    x_rad = x % (2 * pi)
    if x_rad > pi:
        x_rad = x_rad - 2 * pi
    
    target = cos(x_rad) 
    
    res = 0.0
    term = 1.0 
    n = 0
    
    while abs(term) >= eps and n < 500:
        res += term
        n += 1
        term = -term * x_rad * x_rad / ((2*n - 1) * (2*n))
    
    return (res, target, n)

