"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-01-16"
-------------------------------------------------------
"""
# Imports
from Food import Food
from Food_utilities import read_food
#Constants
line = input("Enter data: ")
f = read_food(line)
print(f)
