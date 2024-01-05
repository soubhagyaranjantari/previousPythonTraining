l1=[1,10,2,20,3,30,4,40,5,50]
d={}
for i in range(0,len(l1),2):
    d.update({l1[i]:l1[i+1]})
#         d.update({i:l1[i]})
print(d)

