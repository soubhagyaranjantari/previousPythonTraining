def fun(n):
    for i in range(n):
        yield i
        
f=fun(10)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))


# print(next(f()))