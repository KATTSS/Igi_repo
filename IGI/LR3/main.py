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
import str_analyser as stra

def task_1():
    """Performs main logic for task 1"""
    out.print_task_annotation(1, "Calculate cos(x) with power series and math.cos().")
    
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
    "\n\tStops after entering '100'.")

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

def task_3():
    """Performs main logic for task 3."""
    out.print_task_annotation(3, "Count amount of lowercase symbols and digits in a string.")

    s = inp.get_user_string()

    print(f"Amount of lowercase symbols: {stra.find_lowercase_count(s)}")
    print(f"Amount of digits: {stra.find_digit_count(s)}")

# task_3()

def task_4():
    """Performs main logic for task 4."""
    out.print_task_annotation(4, "1. Count the number of words that begin with a consonant letter;\n" \
    "\t2. Find words with double letters, count their amount;\n" \
    "\t3. Print words in alphabet order.")

    s = "So she was considering in her own mind, " \
    "as well as she could, for the hot day made her feel very sleepy and stupid, " \
    "whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, " \
    "when suddenly a White Rabbit with pink eyes ran close by her."

    print(f"1: Amount of words started with consonant: {stra.count_consonant_starters(s)}")

    doubles = stra.find_double_letter(s)
    print(f"2: Amount of words with double letters: {len(doubles)}\n\t", doubles)

    print(f"3: Sorted by alphabet string:\n{stra.alphabet_sort(s)}")

# task_4()