class one:
    def __init__(self, *args: object) -> None:
        self.args = args
    def display(self):
        print(self.args)
o=one(1,2,1,3,1,4,1,5,1,6,1,7,1,8,1,9)
o.display()
class one:
    def __init__(self, **args: object) -> None:
        self.args = args
    def display(self):
        print(self.args)
o=one(a=1,b=2,c=3)
o.display()
o1=one(name="ABC",loc="ANY")
o1.display()