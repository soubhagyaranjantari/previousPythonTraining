l1=[1,2,3,4,5,5,6,10]
even=0
odd=0
c=0
for i in l1:
    c+=1
    if i%2==0:
        even+=1
    else:
        odd+=1
print(even,":",odd,c)