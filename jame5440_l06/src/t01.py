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

new_list.append(foods[2])

new_list.prepend(foods[0])

new_list.insert(1, foods[1])

for value in new_list:
    print(value)
    print()