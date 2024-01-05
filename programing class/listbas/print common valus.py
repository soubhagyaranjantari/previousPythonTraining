l1=[10,20,30,40,50,10,20]
l2=[10,60,70,50,20,50]
# l3=set()
# for i in l1:
#     for j in l2:
#         if i==j:
#             l3.add(i)

# print(list(l3))
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)
