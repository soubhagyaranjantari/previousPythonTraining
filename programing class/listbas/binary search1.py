l1=[10,22,32,44,54,64,74,84,94]
n=int(input('N:c'))
find=0
f=0
l=len(l1)-1
while f<l and find==0:
    m=(f+l)//2
    if l1[m]==n:
        find+=1
    if l1[m]<n:
        f=m+1
    if l1[m]>n:
        l=m-1
    if l1[f]==n:
        m=f
        find=1
    if l1[l]==n:
        m=l
        find=1
if find==1:
    print('Element found at ',m+1)
else:
    print('Element not found ')
