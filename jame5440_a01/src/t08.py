"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-01-11"
-------------------------------------------------------
"""
# Imports
from functions import matrix_stats
# Constants
a = [[0,1],[2,3],[4,5],[6,7],[8,9]]
small,large,total,average = matrix_stats(a)
print(f"""smallest = {small}
largest = {large}
total = {total}
average = {average}
""")