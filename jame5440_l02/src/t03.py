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
from utilities import array_to_stack,stack_to_array
# Constants
s = Stack()
s._values = []
target = []
print(f'Stack: {s._values}')
c = stack_to_array(s, target)

print(f'Target: {target}')