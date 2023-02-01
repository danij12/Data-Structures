"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Daniel James
ID:      210265440
Email:   jame5440@mylaurier.ca
__updated__ = "2022-01-23"
-------------------------------------------------------
"""
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List
from copy import deepcopy

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) != 0 :
        a = source.pop()
        stack.push(a)
    return

def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    s = []
    temp = Stack()
    while not stack.is_empty(): 
        s.append(stack.pop())
    for a in s:
        temp.push(a)
    while not temp.is_empty():
        b = temp.pop()
        target.append(b)
    return
def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    s = Stack()
    if s.is_empty():
        print(f'is_empty on empty stack: {s.is_empty()}')
        print()
        for a in source:
            s.push(a)
    if not s.is_empty():
        print(f'is_empty on stack with data: {s.is_empty()}')
        print()
        print(f'peek: {s.peek()}')
        print()
        print(f'push: {source[0]}')
        s.push(source[0])
        print()
        print(f'pop: {s.pop()}')
    else:
        print(f'Stack is Empty')

def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) != 0:
        queue.insert(source.pop(0))
    return 

def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not queue.is_empty():
        target.append(queue.remove())
    return None

def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()
    if q.is_empty():
        print(f'is_empty on empty queue: {q.is_empty()}')
        print()
        for i in a:
            q.insert(i)
    if not q.is_empty():
        print(f'is_empty on queue with data: {q.is_empty()}')
        print()
        print(f'peek: {q.peek()}')
        print()
        print(f'insert: {a[0]}')
        q.insert(a[0])
        print()
        print(f'remove: {q.remove()}')
    else:
        print(f'Queue is Empty')

    return

def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for value in source:
        pq.insert(value)
    for _ in range(len(source) - 1, -1, -1):
        source.pop()

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(pq) > 0:
        value = pq.remove()
        target.append(value)

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    
    print(pq.is_empty())
    array_to_queue(pq, a)
    value = pq.remove()
    pq.insert(value)
    print(pq.peek())
    print(pq.remove())

    # tests for the priority queue methods go here
    # print the results of the method calls and verify by hand

    return

def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for _ in range(len(source) - 1, -1, -1):
        llist.insert(0, source.pop())
    return

def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for a in range(len(llist) - 1, -1, -1):
        target.insert(0, llist.pop())
    return

    
    
def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()
    value = source[1]
    print(lst.remove(value))
    print()
    print(lst.is_empty())
    print()
    print(lst.count(value))
    print()
    array_to_list(lst, source)
    lst.append(value)
    lst.remove(value)
    print(lst.remove(value))
    print()
    lst.insert(0, value)
    print(lst[0])
    print()
    print(lst.is_empty())
    print()
    print(lst.count(value))
    print()
    print(lst.max())
    print()
    print(lst.min())
    print()
    print(lst.index(value))
    print()
    print(lst.find(value))

    return