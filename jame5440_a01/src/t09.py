"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-01-13"
-------------------------------------------------------
"""
# Imports
from functions import pig_latin
# Constant
word = input('Enter a word: ')
pl = pig_latin(word)
print(f'Pig-Latin: {pl}')