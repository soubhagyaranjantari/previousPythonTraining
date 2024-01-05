n=40
a=n
while n>0:
    r=n%10
    q=n//10
    n//=10 
mul=r*q
s=r+q
if mul+s==a:
    print('special number')
else:
    print('not special') 
