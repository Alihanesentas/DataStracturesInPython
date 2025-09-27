''' 
LAST IN FIRST OUT 
The functions associated with stack are:

empty()  Returns whether the stack is empty  Time Complexity: O(1)
size()  Returns the size of the stack  Time Complexity: O(1)
top()  Returns a reference to the topmost element of the stack  Time Complexity: O(1)
push(a) Inserts the element ‘a’ at the top of the stack  Time mplexity: O(1)
pop()  Deletes the topmost element of the stack  Time Complexity: O(1)

'''
stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print('Initial Stack')
print(stack)
print("\n Elements popped from stack :" )
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\n Stack after elements are popped \n')
print(stack)

# Implamantation using collections.deque
from collections import deque
stack = deque()
stack.append('g')
stack.append('f')
stack.append('g')
print('Initial stack: ')
print(stack)


# pop() function to pop
# element from stack in
# LIFO order
print('\n Elements popped from stack: ')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\n Stack after elements are popped' )
print(stack)

# Implementation using queue module
from queue import LifoQueue
stack = LifoQueue(maxsize =3 )
print(stack.qsize())
stack.put('g')
stack.put('f')
stack.put('g')

print("Full ", stack.full()) 
print("Size ", stack.qsize()) 

print('\n Elements poppped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())
print("\n Empty ", stack.empty())
