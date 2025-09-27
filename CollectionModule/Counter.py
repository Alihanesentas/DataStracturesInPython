from collections import Counter
print(Counter(['B','B','A','B','C','A','B','B','A','C']))
count = Counter({'A':3,'B':5,'C':2})
print(count)
count.update(['A',1])
print(count)

