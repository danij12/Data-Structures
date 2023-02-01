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
from Food_utilities import read_foods,calories_by_origin
# Constants
line = input("Enter file: ")
origin = int(input('Enter origin number: '))
fv = open(line,"r")
foods = read_foods(fv)
fv.close()
avg = calories_by_origin(foods,origin)
print(f'The average calories is: {avg}')
