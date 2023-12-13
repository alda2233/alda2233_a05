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
from functions import calories_treadmill
# Constants

per_min = float(input("Enter the calories burned per minute: "))
minutes = int(input("Enter the total number of minutes run: "))

calories_treadmill(per_min, minutes)
