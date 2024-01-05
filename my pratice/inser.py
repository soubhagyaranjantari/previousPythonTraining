l1=[1,2,3,5,12,17,2]
for i in range(1,len(l1)):
    f=l1[i]
    j=i-1
    while j>=0 and f<l1[j]:
        l1[j+1]=l1[j]
        j=j-1
    l1[j+1]=f
print(l1)




