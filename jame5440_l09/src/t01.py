"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-03-20"
-------------------------------------------------------
"""
from Food_utilities import get_food
from functions import hash_table


food1 = get_food()

print()
food2 = get_food()

print()
hash_table(4, [food1, food2])