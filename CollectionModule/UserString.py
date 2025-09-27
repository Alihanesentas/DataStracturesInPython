from collections import UserString
class MyString(UserString):
    def append(self,s):
        self.data += s
    def remove(self,s):
        self.data = self.data.replace(s, "")
s1 = MyString("Geeks")
print("Originally String:",s1.data)
s1.append("s")
print("String after appending: ",s1.data)
s1.remove("e")
print("String after removing:",s1.data)
