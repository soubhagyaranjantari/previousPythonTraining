l1=[10,22,32,44,54,64,74,84,94]
n=int(input('N:'))
f=0
l=len(l1)-1
while f<=l:
    m=(f+l)//2
    if l1[m]>n:
        l=m-1
    elif l1[m]<n:
        f=m+1
    else:
        print(f'found at {m}')
        break
else:
    print('not found')