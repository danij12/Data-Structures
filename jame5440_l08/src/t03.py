"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-03-13"
-------------------------------------------------------
"""
from BST_linked import BST
from morse import DATA1, fill_letter_bst


bst = BST()

fill_letter_bst(bst, DATA1)

for value in bst:
    print(value.letter, value.code)