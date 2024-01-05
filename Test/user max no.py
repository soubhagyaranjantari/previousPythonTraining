l1=[22,11,44,33,121,66,125,60]
for i in range(len(l1)-1):
    minv=i
    for j in range(i,len(l1)):
        if l1[minv]<l1[j]:
            minv=j
    l1[minv],l1[i]=l1[i],l1[minv]
print(l1)
a=(l1[:int(input('Enter The Find Out the Max. Number:'))])
for i in a:
    print(i,end=',') 