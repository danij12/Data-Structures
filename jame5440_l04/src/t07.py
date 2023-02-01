"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-02-06"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
from utilities import list_test
# Constants

file = open("food.txt", "r")

source = read_foods(file)

file.close()

list_test(source)