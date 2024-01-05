n=145
e=n
s=0
while n>0:
    fact=1
    rem=n%10
    for i in range(rem,0,-1):
        fact=fact*i
    s=s+fact
    n//=10

if e==s:
    print('strong')
else:
    print('not strong')

# print(s)
