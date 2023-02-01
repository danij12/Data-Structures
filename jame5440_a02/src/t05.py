"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-01-22"
-------------------------------------------------------
"""
from Food import Food
from Food_utilities import read_foods,food_search
# Constants
line = input("Enter file: ")
print()
fv = open(line,"r")
foods = read_foods(fv)
fv.close()
result = food_search(foods,7,1200,False)
for a in result:
    print(f'{a}')
    print()
