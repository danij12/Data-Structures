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
from functions import gcd
# Constants
m = int(input('Enter a number: '))
n = int(input('Enter a second number: '))
ans = gcd(m, n)
print(f'{ans}')