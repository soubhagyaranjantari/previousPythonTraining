s1=input('Enter a string\n')
u,l,s,n=False,False,False,False
for i in s1:
    if ord('A')<=ord(i)<=ord('Z'):
        u=True
    elif ord('a')<=ord(i)<=ord('z'):
        l=True
    elif i in '0123456789':
        n=True
    else:
        s=True
if u and l and s and n and len(s1)>6:
    print('accept')
else:
    print('invalid')