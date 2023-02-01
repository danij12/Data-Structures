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
from functions import is_palindrome_stack
string = input("Enter a sentence: ")
palindrome = is_palindrome_stack(string)
print(f'Palindrome: {palindrome}')