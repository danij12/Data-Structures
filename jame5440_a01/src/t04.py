"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-01-09"
-------------------------------------------------------
"""
# Imports
from functions import is_leap_year
# Constants
year = int(input('Enter a year: '))
leap_year = is_leap_year(year)

print(f'{leap_year}')