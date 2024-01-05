n=int(input('N:'))
b=0
i=0
while n>0:
    r=n%10
    b=b+r*2**i
    i+=1
    n=n//10
print(b)

