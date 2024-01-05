l1=[1,2,3,4,5,6,7,8,9,0,0,0]
n=int(input())
l2=[]
for i in range(0,len(l1)-1,n):
    l3=[]
    for j in range(i,i+n):
        if j<len(l1):
            l3.append(l1[j])
    l2.append(l3)
print(l2)