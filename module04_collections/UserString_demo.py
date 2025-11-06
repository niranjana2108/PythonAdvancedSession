from collections import UserString

class UString(UserString):
    def add(self, char): #adding a character
        self.data = self.data+char
    def modify(self,char1,char2): #change a character
        self.data=self.data.replace(char1,char2)
uStr=UString("PythomGeek")
print(uStr)
uStr.add('s')
print(uStr)
uStr.modify('m','n')
print(uStr)
