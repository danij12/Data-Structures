"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-01-21"
-------------------------------------------------------
"""
from Food import Food
from Food_utilities import read_foods,food_table
# Constants
line = input("Enter file: ")
print()
fv = open(line,"r")
foods = read_foods(fv)
fv.close()
avg = food_table(foods)
print(f'{avg}')
