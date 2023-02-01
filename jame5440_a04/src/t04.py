"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-02-05"
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue
from functions import pq_split_key

source = Priority_Queue()

source.insert(1)

source.insert(2)

source.insert(3)

key = 2

target1, target2 = pq_split_key(source, key)


print("Target 1: ")
while len(target1) > 0:
    print(target1.remove())

print("Target 2: ")
while len(target2) > 0:
    print(target2.remove())