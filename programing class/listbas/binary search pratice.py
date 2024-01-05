l=[1,2,3,4,5,6,7,8,9]
n=int( input ('Enter a number:'))
f=0
i=0
ui=len(l)
while i<=ui and f==0:
    mid = (i+ui)//2
    if l[mid]==n:
        p=mid+1
        f==1
    if l[mid]<n:
        i=mid+1
    if l[mid]>n:
        ul=mid-1
if f==1:
        print(f'{n} found at positino',p)
else:
        print(f'{n} not found')
# wrong
