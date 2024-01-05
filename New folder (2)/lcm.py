a=int(input('A:'))
b=int(input('B:'))
if a>0 and b> 0:
    c=1
    for i in range(2,a+1):
        if a%i==0 and b%i==0:
            c=c*i
print(c)            
            # break