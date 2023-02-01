"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-01-15"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze
# Constants
file = input("Enter file name: ")
fv = open(file,"r")
u,l,d,w,r = file_analyze(fv)
fv.close()
print(f"""u = {u}
l = {l}
d = {d}
w = {w}
r = {r}
""")

