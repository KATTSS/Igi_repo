"""LR3/igi
Output module
Version: 1.0
Author: Ekaterina Butkevich
Group: 453501
Date: 10.03.2026
"""

from math import log10

def print_table(**kwargs):
    """Prints a formatted table from passed dictionary."""
    headers = list(kwargs.keys())
    values = list(kwargs.values())

    eps_value = kwargs.get('eps', 0.01)
    precision = max(0, -int(log10(eps_value))) + 1 
    
    formatted_values = []
    for v in values:
        if isinstance(v, float):
            formatted_values.append(f"{v:.{precision}f}")
        else:
            formatted_values.append(str(v))
    
    col_widths = [max(len(str(h)), len(str(v))) for h, v in zip(headers, formatted_values)]
    
    header_row = " | ".join(str(h).ljust(w) for h, w in zip(headers, col_widths))
    print("-" * len(header_row))
    print(header_row)
    print("-" * len(header_row))
    
    value_row = " | ".join(str(v).ljust(w) for v, w in zip(formatted_values, col_widths))
    print(value_row)
    print("-" * len(header_row))


def print_task_annotation(task_num, annotation):
    """Prints a string 'Task {Task num}: {Task annotation}'."""
    print(f"\nTask {task_num}: {annotation}")

def print_menu():
    """Prints a list of lab tasks."""

    print("\n1. Calculate power series;\n" \
          "2. Sequence operations;\n" \
          "3. Keyboard text handler; \n" \
          "4. Hardcoded text analyser; \n" \
          "5. Numeric list operations;\n" \
          "6. Exit all.\n" \
          "\nEnter yuor choice:")
