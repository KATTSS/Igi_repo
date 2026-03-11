"""LR3/igi
Main lab module
Version: 1.0
Author: Ekaterina Butkevich
Group: 453501
Date: 10.03.2026
"""

# Module connection
import my_math as mth
import input as inp
import output as out

def task_1():
    """Performs main logic for task 1"""
    out.print_task_annotation(1, "Calculate cos(x) with power series and Math.cos()")
    
    print("Enter x:")
    x=inp.get_user_int()

    print("Enter eps:")
    eps=inp.get_user_float()

    results=mth.row_calcilator(x, eps)
    out.print_table(**{'x':x, 'n':results[2], 'F(x)':results[0], 'Math F(x)':results[1], 'eps':eps})


# task_1()

def task_2():
    """Performs main logic for task 2"""
    out.print_task_annotation(2, "Calculate sum for a numeric sequence," \
    " count amount of elements < 10." \
    "\n\tStops after entering '100'")

    sequence_sum=0
    amount_smaller_10=0

    while True:
        x=inp.get_user_int()
        if x==100:
            print(f"Sum = {sequence_sum}")
            print(f"Amount of sequence elements smaller than 10: {amount_smaller_10}")
            return
        elif x<10:
            amount_smaller_10 +=1
        sequence_sum +=x

# task_2()
