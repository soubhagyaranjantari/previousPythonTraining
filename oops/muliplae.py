class metro:
    def __init__(self):
        self.i1='mango'
        self.i2='apple'
    def metro_item(self):
        print(self.i1)
        print(self.i2)
class d_mart:
    def __init__(self):
        self.a='cake'
        self.i4='juice'
    def dmart_item(self):
        print(self.a)
        print(self.i4)
class aa_mart():
    def __init__(self):
        self.i5='cigirate'
        self.i6='alchol'
    def aa_mart_item(self):
        print(self.i5)
        print(self.i6)
class mix(metro,d_mart,aa_mart):
    def __init__(self):
        metro.__init__(self)
        d_mart.__init__(self)
        aa_mart.__init__(self)
        self.a='kanhu'
        self.aaa='*'
    def mix1(self):
        print(self.a)
        print(self.aaa)
o=mix()
o.dmart_item()
o.metro_item()
o.aa_mart_item()
o.mix1()

