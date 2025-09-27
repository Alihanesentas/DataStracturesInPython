'''
Tuple's are similiar to list but unlike the list,
they cannot be changed after their creation.
* Tuples can hold different data types
* Ordered
'''
# Creating a Tuple
tup = ()
print(tup)
tup = ('Geeks', 'For')
print(tup)
#Using list
li = [1,2,3,4,5]
print(tuple(li))
#Using built-in funcitons
tup = tuple('Geeks')
print(tup)

#Creating Tuple mix data types

tup = (5, 'Welcome', 7, 'Geeks')
print(tup)

# Creating a Tuple with nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)
print(tup3)

# Creating a Tuple with repetition
tup1 = ('Geeks',) * 3
print(tup1)

# Creating a Tuple with the use of loop
tup = ('Geeks')
n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup)

'''
Python Tuple Basic Operations
Below are the Python tuple operations.

Accessing of Python Tuples
Concatenation of Tuples
Slicing of Tuple
Deleting a Tuple
Accessing of Tuples
We can access the elements of a tuple by using indexing and slicing, similar to how we access elements in a list. Indexing starts at 0 for the first element and goes up to n-1, where n is the number of elements in the tuple. Negative indexing starts from -1 for the last element and goes backward.
'''
# Accesing Tuple with indexing
tup = tuple("Geeks")
print(tup[0])
print(tup[1:4])
print(tup[:3])

# Tuple unpacking
tup = ("Geeks","For","Geeks")
a,b,c = tup 
print(a)
print(b)
print(c)
 
# Concatentation of Tuples
tup1 = (0,1,2,3,4,5)
tup2 = ('Geeks','For','Geeks')
tup3 = tup1 + tup2
print(tup3)

#Slicing of Tuple
tup = tuple('GEEKSFORGEEKS')
print(tup[1:])
print(tup[::-1]) # Reversing
print(tup[4:9])

#Deleting Tuple
tup = (0,1,2,3,4)
del tup
print(tup)
