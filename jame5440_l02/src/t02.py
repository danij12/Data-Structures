"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-01-23"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack
# Constants
s = Stack()
source = [1,2,3]
print(f'Array: {source}')
b = array_to_stack(s,source)
values = s._values
print(f'Stack: {values}')
