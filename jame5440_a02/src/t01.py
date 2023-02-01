"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-01-18"
-------------------------------------------------------
"""
# Imports
from Food import Food
from Food_utilities import read_foods,by_origin
# Constants
line = input("Enter file: ")
origin = int(input("Enter Origin number: "))
print()
fv = open(line,"r")
foods = read_foods(fv)
fv.close()
v = by_origin(foods, origin)
for a in v:
    print(a)
    print()