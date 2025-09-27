# Creating List
a = [1,2,3,4,5]
b = ['apple','banana','cherry']
c = [1,'hello',3.14,True]
print(a)
print(b)
print(c)

#Using List() Consturctor
a = list((1,2,3,'apple',3.4))
print(a)

b = list("GFG")
print(b)

# Creating List with Repeated Elements
a = [2] * 5
b = [0] * 7
print(a)
print(b)

# Accesing List elements
a = [10,20,30,40,50]
print(a[0])
print(a[-1])
print(a[1:4]) # elements from index 1 to 3

#Adding elements into list
a = []
a.append(10)
print("After append(10): ",a)
a.insert(0,5)
print("After insert(0,5): ",a)
a.extend([15,25,35]) # extend will seperate a list charachters
print("After extend([15,25,35]): ",a)
a.append([15,25,35])
print("After append([15,25,35]): ",a)
a.clear()
print("After clear(): ",a)

# Updating elements into list 
a = [1,23,4,5,61,3,1,2]
a[1] = 25
print(a)

# Removing elements from list
a = [1,2,3,4,5,6,7,8,9,10]
a.remove(10)
print("After remove(10): ",a)

popped_val = a.pop(1)
print("Popped element: ",popped_val)
print("After pop(1):",a)
del a[0]
print("After del a[0]: ",a)

# Iterating Over List
a = ['apple','banana','cherry']
for item in a:
    print(item)

#Nested Skills
matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]
print(matrix[1][2])

# List Comprehension 
squares = [x**2 for x in range(1,6)]
print(squares)

