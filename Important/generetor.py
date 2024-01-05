def  function():
    yield 1
    yield 2
    yield 3
    yield 4
# print(function())
# print(function())
# print(function())
f=function()
print((f.__next__()))
print((f.__next__()))
print((f.__next__()))
print(next(f))
# print((f.__next__()))