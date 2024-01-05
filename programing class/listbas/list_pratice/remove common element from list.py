l1=[1,2,3,4,5,6,7,8,1,2,3,4,2,2,3,4,50]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)