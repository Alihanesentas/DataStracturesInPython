'''
A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries. When a key is needed to be found then all the dictionaries are searched one by one until the key is found.
'''
from collections import ChainMap

d1 = {'a': 1, 'b': 2} 
d2 = {'c': 3, 'd': 4} 
d3 = {'e': 5, 'f': 6} 
c = ChainMap(d1,d2,d3)
print(c)