d={1:10,2:20,3:30,4:40,5:50}
# l1=[i for i,j in d.items()]
# l2=[j for i,j in d.items()]
l1=[]
l2=[]
for i in d:
    l1.append(i)
    l2.append(d[i])
print(l1,l2)
