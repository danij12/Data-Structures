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

from Stack_array import Stack,combine
# Constants
s = Stack()
source1 = Stack()
source2 = Stack()
source1._values = [5,8,12,8]
source2._values = [3,6,1,7,9,14]
target = combine(s,source1, source2)
print(s._values)

