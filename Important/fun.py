def fun():
    print(f'Hello world1')
hlo=fun
# hlo()
# fun()
def fun2(hlo):
    fun()
    print('Hello world2')
# fun2(5)
l=lambda n: (n%2)
print(l(10))