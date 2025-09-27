from collections import UserDict

class MyDict(UserDict):
    def __del__(self):
        raise RuntimeError("Deletion not allowed")
    def pop(self,s=None):
        raise RuntimeError("Deletion not allowed")
    def popitem(self,s=None):
        raise RuntimeError("Deletion not allowed")
d = MyDict({'a':1,
                'b':2,
                'c':3})
print(d)    
d.pop(1)