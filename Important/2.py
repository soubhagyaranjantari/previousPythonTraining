s='THIS IS A - GOOD BOY - AND HE - IS GOOOD'
l1=s.split()
l2=list(map(len,l1))
res=None
for i in l1:
    if max(l2)==i:
        res=i
print(i)
print(l2)