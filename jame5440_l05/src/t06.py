"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-02-20"
-------------------------------------------------------
"""
# Imports
from functions import bag_to_set
# Constants
bag = [11,22,33,44,55]
print(f'Old: {bag}')
new_set = bag_to_set(bag)
print(f'New: {new_set}')