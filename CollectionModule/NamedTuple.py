from collections import namedtuple
student = namedtuple('student',['name','age','DOB'])
S = student('Nandini','19','232212')
print(S[1])
print(S.name)
