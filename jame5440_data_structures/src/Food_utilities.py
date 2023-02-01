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
from copy import deepcopy
from Food import Food
from pickle import FALSE, NONE
from pip._vendor.html5lib.treewalkers.base import NonRecursiveTreeWalker


def get_food():
    """
    -------------------------------------------------------
    Creates a food object by requesting data from a user.
    Use: f = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """
    Name = input("Name: ")
    list_foods = Food.origins()
    print(f'Origin')
    print(list_foods)
    Origin = int(input(": "))
    Vegeterian = input("Vegeterian (Y/N): ")
    Calories = int(input("Calories: "))
    if Vegeterian == "Y":
        Vegeterian = True 
    else:
        Vegeterian = False 
    food = Food(Name,Origin,Vegeterian,Calories)

    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a food object from a line of string data.
    Use: f = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """
    name = ""
    origin = 0
    is_vegeterian = None
    calories = 0
    line2 = line.split("|")
    if line2[0] != "":
        name = line2[0]
    if line2[1].isdigit():
        origin = int(line2[1])
    if line2[2] == "True":
        is_vegeterian = True
    elif line2[2] == "False":
        is_vegeterian = False
    calories = int(line2[3])
    food = Food(name,origin,is_vegeterian,calories)



    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """
    foods = []
    for a in file_variable:
        foods.append(read_food(a))
        

    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    for food in foods: 
        food.write(file_variable) 

    # Your code here

    return


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian foods.
    foods is unchanged.
    Use: v = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """
    veggies = []
    for food in foods: 
        if food.is_vegetarian: 
           veggies.append(food)
    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of foods by origin.
    foods is unchanged.
    Use: v = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    origins = []
    temp = "" 

    for a in range(len(foods)):
        temp = f'{foods[a]}'
        if Food.ORIGIN[origin] in temp:
            origins.append(foods[a])

    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """
    avg = 0 
    count = 0
    temp =None
    
    for a in range(len(foods)):
        temp = foods[a]
        avg += temp.calories
        count += 1
    avg /=count

    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: a = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    avg = 0 
    count = 0
    temp = None
    
    for a in range(len(foods)):
        temp = foods[a]
        if Food.ORIGIN[origin] == Food.ORIGIN[temp.origin]:
            avg += temp.calories
            count += 1
    avg /=count


    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of foods, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    temp = None
    temp_foods = deepcopy(foods)
    temp_foods.sort()
    print(f'Food                               Origin       Vegetarian Calories')
    print(f'----------------------------------- ------------ ---------- --------')
    for a in range(len(foods)):
        temp = temp_foods[a]
        print(f'{temp.name:<35}  {Food.ORIGIN[temp.origin]:<16} {temp.is_vegetarian!s:<10} {temp.calories:<25}')
        

    return

def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for foods that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))
    result = []
    temp = None
    for a in range(len(foods)):
        temp = foods[a]
        if (origin == -1 or temp.origin == origin) and (max_cals == 0 or temp.calories <= max_cals) and (not is_veg or temp.is_vegetarian):
            result.append(temp)
        

    return result
