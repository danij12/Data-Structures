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
from functions import reroute
# Constants
opstring =  input('Enter a string: ')
values_in = [1,2,3,4]
values_out = reroute(opstring, values_in)
print(f'{values_out}')