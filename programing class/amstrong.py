n=153
a=n
b=n
s=0
i=0
j=0
while n>0:
    n=n//10
    i+=1
# print(i)    
while a>0:
    rem=a%10
    s=rem**i
    a=a//10
    j=j+s
if j==b:
    print('armstrong number')

else:
    print('not armstrong numebr')