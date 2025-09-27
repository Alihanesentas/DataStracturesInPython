from collections import OrderedDict
print("Before deleting: \n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
od['f'] = 5
for key, value in od.items():
    print(key,value)
print("\n After deleting:\n")
od.pop('c')
for key,value in od.items():
    print(key,value)
print("\n After re-instering : \n")
od['c'] = 3
for key,value in od.items():
    print(key,value)
 