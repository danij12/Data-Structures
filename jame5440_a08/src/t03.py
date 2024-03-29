"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-03-19"
-------------------------------------------------------
"""
from BST_linked import BST
from Letter import Letter
from functions import do_comparisons, letter_table

# Takes a long time to compute

DATA = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst = BST()

for value in DATA:
    letter = Letter(value)
    bst.insert(letter)

file = open('gibbon.txt', 'rt')

do_comparisons(file, bst)

file.close()

letter_table(bst)