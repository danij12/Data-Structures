"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-01-08"
-------------------------------------------------------
"""
# Imports
from functions import dsmvwl

# Constants
s = input("Sentence: ")
out = dsmvwl(s)

print(f'Disemvowelled: {out}')
