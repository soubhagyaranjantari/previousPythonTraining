n=int(input())
l1=[10,20,30,40,50]
c=0
d=0
for j in range(n):
    t=l1[0]
    c+=1
    for i in range(len(l1)-1):
        d+=1
        l1[i]=l1[i+1]
    l1[len(l1)-1]=t
print(l1,c,d)