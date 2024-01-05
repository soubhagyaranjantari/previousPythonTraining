class one:
    a=11
    b=111
    def __init__(self,name,age):
        self.a=22
        self.b=33
        self.name=name
        self.age=age
    def asd(self):
        print('hello')

class two(one):
    a=111
    def __init__(self,name,age):
        super().__init__(name=name,age=age)
        a=123
        y=12345
o2=two('anil',25)

o2.asd()




        