l1=[1,2,3,4,5]
l2=[10,20,30,40,50]
d={}
# l3=len(l1)
if len(l1)==len(l2):
    for i in range(len(l1)):
        d.update({l1[i]:l2[i]})
print(d)

