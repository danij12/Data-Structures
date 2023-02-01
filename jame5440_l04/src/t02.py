"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-02-05"
-------------------------------------------------------
"""
from Food import Food
from List_array import List
s = Food("Spring Rolls", 1, None, None)
a = Food("BBQQ Pork", 1, None, None)
b = Food("Poutine", 0, None, None)
c = Food("Crepe", 7, None, None)
d = Food("Spring Rolls", 1, None, None)
target = List()
target._values = [a,d,b,c]
i = target._linear_search(s)
print(f'{i}')