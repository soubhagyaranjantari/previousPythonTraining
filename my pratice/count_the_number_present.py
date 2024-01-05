n=int(input('Enter a number to reverse\n'))
a=0
while n>0:
    if n%10==0:
        a+=1
    n=n//10
print(a)