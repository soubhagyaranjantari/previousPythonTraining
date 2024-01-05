l1=[1,55,33,22,11,444,33,1,-1,0]
c=0
for i in range(len(l1)-1):
    for j in range(len(l1)-1-i):
        if l1[j]>l1[j+1]:
            l1[j+1],l1[j]=l1[j],l1[j+1]
            c+=1
    print(len(l1)-1-i)
print(l1,c)
