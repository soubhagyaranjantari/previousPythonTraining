l1=[1,2,34,-1,11,44,4546546545,4,56,55,-15]
f=0
s=0
c=0
for j in range(len(l1)-1):
    f+=1
    for i in range(len(l1)-1-j):
        c+=1
        if l1[i]>l1[i+1]:
            l1[i],l1[i+1]=l1[i+1],l1[i]
            s+=1
print(l1)
print(f,"  ",s,c)































