"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-01-28"
-------------------------------------------------------
"""
from Stack_array import Stack
from copy import deepcopy
from pickle import TRUE, NONE
def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    index = 1
    while (not source1.is_empty()) or (not source2.is_empty()):
        if (index % 2 == 0) and (not source2.is_empty()) or source1.is_empty():
            value = source2.pop()
            target.push(value)
        else:
            value = source1.pop()
            target.push(value)
        index += 1
    return target
def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    temp = []
    while not source.is_empty():
        temp.append(deepcopy(source.pop()))
    while len(temp) != 0:
         source.push(temp.pop(0))
    
    return
def reverse(self):
    """
    -------------------------------------------------------
    Reverses the contents of the source stack.
    Use: source.reverse()
    -------------------------------------------------------
    Returns:
        None
    -------------------------------------------------------
    """
    temp = [] 
    while len(self._values)>0:
        temp.append(self._values.pop())   
    while len(temp)>0:
        self._values.append(temp.pop(0))
    return

def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    s = Stack()
    count = 0 
    temp = ""
    temp2 = None
    palindrome = True
    string = string.lower()
    for a in range(len(string)):
        if string[a].isalpha():
            temp += string[a]
    while count < len(temp)/2:
        s.push(temp[count])
        count +=1
    if len(temp)%2 != 0:
        s.pop()
    while count < len(temp) and palindrome:
        temp2 = s.pop()
        if temp2 != temp[count]:
            palindrome = False 
        else:
            count +=1
    return palindrome
def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """
    s = Stack()
    values_out = []
    valid = True 
    string = ['S','X']
    count = 0 
    temp1 = 0
    temp2 = 0
    temp3 = None
    while count < len(opstring) and valid:
        if opstring[count] not in string:
            values_out = None 
            valid = False
        count +=1
    
    while temp1 < len(opstring) and valid:
        if opstring[temp1] == 'S' and temp2 < len(values_in):
            s.push(values_in[temp2])
            temp2 +=1
        elif opstring[temp1] == 'X' and not s.is_empty():
            temp3 = s.pop()
            values_out.append(temp3)
        temp1 +=1
    return values_out
                