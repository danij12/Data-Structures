"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-03-06"
-------------------------------------------------------
"""
from List_linked import List

lst1 = List()

lst2 = List()

array = [1, 2, 3, 4, 5]

array2 = [1, 2, 3, 4, 5]

for value in array:
    lst1.append(value)

for value in array2:
    lst2.append(value)

print(lst1.is_identical_r(lst2))