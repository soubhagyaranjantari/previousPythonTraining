def fun(n):
    def inner_fun():
        print('!st')
        n()
        print(1,'st')
    return inner_fun
@fun
def fun2():
    print('@nd')
fun2()
