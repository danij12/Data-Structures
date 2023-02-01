"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-02-27"
-------------------------------------------------------
"""
from Food_utilities import read_foods
from List_linked import List


file_variable = open("foods.txt", "r")

foods = read_foods(file_variable)

file_variable.close()

new_list = List()

for value in foods:
    new_list.append(value)

print(new_list.peek())

print()
print(new_list.remove(foods[5]))