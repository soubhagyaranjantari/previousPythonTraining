l1=[10,20,30,40,50]
t=l1[0]
print(l1)
for i in range(len(l1)-1):
    l1[i]=l1[i+1]
l1[len(l1)-1]=t
print(l1)