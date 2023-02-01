"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-01-29"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from functions import stack_reverse
# Constants
source = Stack()
source._values = [5,8,12,8]
print(f'Original: {source._values}')
target = stack_reverse(source)
print(f'Reverse: {source._values}')

