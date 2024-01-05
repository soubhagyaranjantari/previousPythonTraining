class A:
    def __init__(self,a,b,c):
        self.name=a
        self._b=b
        self.__c=c
    def bc(self):
        print('this is a method')
        print(self.name)
        print(self._b)
        print(self.__c)

x=A('kanhu',2,3)
x.bc()

d=5
