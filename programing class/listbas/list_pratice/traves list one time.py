l1=[10,20,30,40,50]
f=l1[0]
for i in range(len(l1)-1):
    l1[i]=l1[i+1]
l1[len(l1)-1]=f
print(l1)