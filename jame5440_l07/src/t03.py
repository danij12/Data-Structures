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

lst = List()

array = [5, 11, 2, 3, 8]

for value in array:
    lst.append(value)

target1, target2 = lst.split_alt_r()

print("Printing Target1: ")
for value in target1:
    print(value)

print()
print("Printing Target2: ")
for value in target2:
    print(value)