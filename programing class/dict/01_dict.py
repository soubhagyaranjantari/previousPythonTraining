# def fun(n):
#     print(n)
#     if n<5:
#         fun(n+1)
#         print(n,end='')
# fun(0)
# def fun(n):
#     print(n,end='')
#     a=ord(n)
#     if a<ord('D'):
#         fun(chr(a+1))
#         print(n,end='')
# fun('A')
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
f=fact(5)
print(f)