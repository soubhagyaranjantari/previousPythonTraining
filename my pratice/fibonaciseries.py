n=int(input('N:'))
a=0
b=1
c=0
for i in range(n):
    print(c,end=' ')
    a=b
    b=c
    c=a+b
# while n>0:
#     print(c,end=' ')
#     a=b
#     b=c
#     c=a+b
#     n=n-1