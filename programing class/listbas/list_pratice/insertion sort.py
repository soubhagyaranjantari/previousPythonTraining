l1=[11,13,1,12,5,33,7,2,0]
l1=[13,5,2,17]
for i in range(1,len(l1)):
    ele=l1[i]
    j=i-1
    while j>=0 and ele <l1[j]:
        l1[j+1]=l1[j]
        j=j-1
    l1[j+1]=ele
print(l1)

# print(13<11)