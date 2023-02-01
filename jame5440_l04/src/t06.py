"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-02-06"
-------------------------------------------------------
"""
from List_array import List
from utilities import array_to_list, list_to_array

llist = List()

source = [1, 2, 3, 4, 5]

array_to_list(llist, source)

print("LList: ")
for value in llist:
    print(value)

list_to_array(llist, source)

print()
print("List: ")
for value in source:
    print(value)