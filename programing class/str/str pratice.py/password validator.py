p=input('Enter Ur Password:')
u,l,i,sp=False,False,False,False
for i in p:
    if ord('A')<=ord(i)<=ord('Z'):
        u=True
    elif ord('a')<=ord(i)<=ord('z'):
        l=True
    elif i in '1234567890':
        i=True
    else:
        sp=True
if u and l and i and sp and len(p)>=8:
    print('Accepted')
else:
    print('Not Accepted')