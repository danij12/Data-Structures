"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-03-12"
-------------------------------------------------------
"""
from Food_utilities import read_foods
from List_linked import List

file = open("food.txt", "rt")

foods = read_foods(file)

file.close()

lst = List()

for value in foods:
    lst.append(value)

print("Printing the first item: ")
print(lst[0])

lst.prepend(foods[10])

print()
print("Printing first item: ")
print(lst[0])


print()
print("Printing count of each item: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in lst:
    print(f"{value.name:35} {lst.count(value):>5}")

lst.clean()

print()
print("Printing count of each item: ")
for value in lst:
    print(f"{value.name:35} {lst.count(value):>5}")

lst2 = List()

lst3 = List()

for value in range(10):
    lst2.append(foods[value])

lst3.combine(lst, lst2)

print()
print("Printing count of each item in lst3: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in lst3:
    print(f"{value.name:35} {lst3.count(value):>5}")


for value in range(20, 26):
    lst.append(foods[value])

lst2.intersection(lst, lst3)

print()
print("Printing count of each item in lst2: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in lst2:
    print(f"{value.name:35} {lst2.count(value):>5}")


print()
print("lst1 and lst2 are identical?: ")
print(lst.is_identical(lst2))

print()
print("Printing the removed value: ")
print(lst.remove_front())


print()
print("Printing count of each item in lst3: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in lst3:
    print(f"{value.name:35} {lst3.count(value):>5}")


lst3.remove_many(foods[0])

print()
print("Printing count of each item in lst3: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in lst3:
    print(f"{value.name:35} {lst3.count(value):>5}")

