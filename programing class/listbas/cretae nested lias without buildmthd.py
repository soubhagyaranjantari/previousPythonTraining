l1=[1,2,3,4,5,6,7,8,9,10,12,13,14]
n=0
l2=[]
for i in range(0,len(l1),n):
    l3=[]
    for j in range(i,i+n) :
        if j<len(l1):
            l3.append(l1[j])
    l2.append(l3)
print(l2)