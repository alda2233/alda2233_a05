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
from functions import range_addition
# Constants

start = int(input("Enter the start value: "))
increment = int(input("Enter the increment value: "))
count = int(input("Enter the number of values to sum: "))

total = range_addition(start, increment, count)
print(total)
