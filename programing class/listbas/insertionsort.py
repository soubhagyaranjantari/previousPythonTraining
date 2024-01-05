l1=[1,2,34,11,44,4,56,55,15,500]
f=0
s=0
for i in range(len(l1)):
    f+=1
    key=l1[i]
    j=i-1
    while (l1[j]>key and j>=0):
        s+=1
        l1[j+1]=l1[j]
        j-=1
        print(l1)  
    l1[j+1]=key
print(l1,f,s)        