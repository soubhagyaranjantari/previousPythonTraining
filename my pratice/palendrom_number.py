n=int(input('Enter a number to reverse\n'))
a=n
reverse=0
while n>0:
    rem=n%10
    reverse=reverse*10+rem
    n=n//10
    
if a==reverse:
    print('this palendrom')
else:
    print("Not Palendrom")
print(n)