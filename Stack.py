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