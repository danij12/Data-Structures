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
from Queue_circular import Queue
from functions import queue_split_alt

source = Queue(3)

source.insert(3)

source.insert(4)

source.insert(5)

target1, target2 = queue_split_alt(source)


print("Target 1: ")
while len(target1) > 0:
    print(target1.remove())

print("Target 2: ")
while len(target2) > 0:
    print(target2.remove())