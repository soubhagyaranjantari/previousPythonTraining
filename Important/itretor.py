# l1=[1,2,3,4,5]
# l=iter(l1)
# print(l.__next__())
# print(l.__next__())
# print(l.__next__())
# print(l.__next__())
# print(next(l))
# print(l.__next__()) Thow error cause index out of range
# s=()
# print(dir(s))
# s1=s.__reduce__()
# print(s1)
class myrange:
    def __init__(self,strat,end) -> None:
        self.strat=strat
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        temp=self.strat
        if self.strat<self.end:
            self.strat+=1
            return temp
        else:
            raise StopIteration
o=myrange(10,15)
n=DeprecationWarning(o)
print(n)
# print(dir(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))
# print(next(o))
print(iter(o))