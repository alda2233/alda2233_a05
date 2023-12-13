"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-11-04"
-------------------------------------------------------
"""
# Imports

# Constants


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """

    if number < 0:
        product = None
    else:
        product = 1
        for i in range(1, number + 1):
            product *= i

    return int(product)


def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    Prints a table of the number of calories burned every five minutes 
    while running on a treadmill, given the number of calories burned per minute (per_min)
    and the total number of minutes run (minutes).

    Use: calories_treadmill(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min - calories burned per minute (float or int)
        minutes - total number of minutes run (int)

    Returns:
        None
    ------------------------------------------------------
    """

    for minute in range(5, minutes + 1, 5):
        calories = per_min * minute
        print(f"{minute}  {calories:.1f}")

    return None


def arrow_up(rows):
    """
    -------------------------------------------------------
    Prints an arrow made of # characters pointing up with the specified number of rows.

    Use: arrow_up(rows)
    -------------------------------------------------------
    Parameters:
        rows - the number of rows in the arrow (int)

    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        if i == 1:
            print(spaces + "#")
        else:
            middle_spaces = " " * (2 * (i - 1) - 1)
            print(spaces + "#" + middle_spaces + "#")

    return None


def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """

    print(" " * 11, end="")
    for i in range(start_num, stop_num + 1):
        print(f"{i:8}", end="")
    print("\n" + " " * 11 + "-" * (9 * (stop_num - start_num + 1)))

    for i in range(start_num, stop_num + 1):
        print(f"{i:2} |", end="")
        for j in range(start_num, stop_num + 1):
            result = i * j
            print(f"{result:8}", end="")
        print()

    return None


def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """

    total = 0
    for _ in range(count):
        total += start
        start += increment
    return total
