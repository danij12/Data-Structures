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

from Stack_array import Stack
from functions import reverse
# Constants
s = Stack()
source1 = Stack()
source1._values = [5,8,12,8]
print(f'Original: {source1._values}')
target = reverse(source1)
print(f'Reverse: {source1._values}')

