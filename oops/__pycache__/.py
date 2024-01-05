class apu:
    ap=4455
    def __init__(self,n,a,) -> None:
        self.n = n
        self.a = a
    def show(self):
        print(f"name is {self.n} age {self.a}")
# a=apu('apu',24)
# a.show()
print(apu.ap)