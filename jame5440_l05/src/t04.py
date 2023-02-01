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
from functions import to_power
# Constants
base = int(input('Enter a base: '))
power = int(input('Enter a power: '))
ans = to_power(base, power)
print(f'Answer: {ans}')