"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-03-05"
-------------------------------------------------------
"""
from Priority_Queue_linked import Priority_Queue

queue = Priority_Queue()

print("Queue is empty: ")
print(queue.is_empty())

print()
print("Length of queue: ")
print(len(queue))

queue.insert(11)

print()
print("Length of queue: ")
print(len(queue))

queue.insert(22)

print()
print("Removed Node: ")
print(queue.remove())

print()
print("First item in queue: ")
print(queue.peek())

queue1 = Priority_Queue()

queue1.insert(44)

queue2 = Priority_Queue()

queue2.combine(queue, queue1)

print()
print("Printing queue2: ")
for value in queue2:
    print(value)

target1, target2 = queue2.split_alt()

print()
print("Printing target1: ")
for value in target1:
    print(value)

print()
print("Printing target2: ")
for value in target2:
    print(value)

queue2.insert(1)

queue2.insert(24)

queue2.insert(36)

queue2.insert(18)

target3, target4 = queue2.split_key(33)

print()
print("Printing target1: ")
for value in target3:
    print(value)

print()
print("Printing target2: ")
for value in target4:
    print(value)