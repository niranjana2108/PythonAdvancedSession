from collections import UserDict
class UDict(UserDict):
    def pop(self, ele=None):
        raise RuntimeError("Not allowed to delete")
    def _del_(self):
        raise RuntimeError("Not allowed to delete")
    def popitem(seld, ele=None):
        raise RuntimeError("Not allowed to delete")
uDic=UDict({'a':1,'e':2,'i':4,'o':4,'u':5})
print(uDic)
uDic['e']=8
print(uDic)
uDic.pop()
