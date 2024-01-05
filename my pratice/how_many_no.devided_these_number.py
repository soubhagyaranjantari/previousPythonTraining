a=int(input('Enter a number to reverse-->'))
b=int(input('Enter a number to reverse-->'))
if a>b:
    maX=a
else:
    maX=b
for i in range(1,maX):
    if a%i==0 and b%i==0:
        print(i,end=',')
