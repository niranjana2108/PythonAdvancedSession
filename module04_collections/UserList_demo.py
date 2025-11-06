from collections import UserList
class UList(UserList):
    def append(self,s=None):
        raise RuntimeError("No more entries allowed")
    def extend(self,s=None):
        raise RuntimeError("No more entries allowed")
    def insert(self,s=None):
        raise RuntimeError("No more entries allowed")
uList=UList([1,3,5,7,9])
print(uList)
uList.pop()
print(uList)
uList.append(6)