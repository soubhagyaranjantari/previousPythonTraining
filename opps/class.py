class emp:
    com='Google'
    sal=1000
    loc='India'
    def changeatt(self,s):
        pass
        self.__class__.sall=s 
    @classmethod
    def changeatt1(cls,c):
        cls.com=c
        cls.sall=3000
    def any(self):
        self.sall=3000
e=emp()
print(e.loc)
print(e.com)
e.changeatt1('Youtube')
print(e.com)
print(e.sal)
e.changeatt(5000)
print(e.sal)
print(e.com)
print(e.sall)

