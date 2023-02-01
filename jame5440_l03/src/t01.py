"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-01-30"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
# Constants
q = Queue()
q._values = [1,2,3]
print(f'Before Insert: {q._values}')
q.insert(4)
print(f'After Insert: {q._values}')