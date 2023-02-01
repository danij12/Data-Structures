"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-02-14"
-------------------------------------------------------
"""
from functions import recurse

x = int(input('Enter a integer number: '))
y = int(input('Enter a second integer number: '))

ans = recurse(x, y)
print(f'{ans}')