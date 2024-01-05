l1=[11,13,1,12,5,3,7,2,0]

l2=l1.copy()
c=0
print(l1)
for i in range(len(l1)-1):
    for j in range(len(l1)-1-i):
        if l1[j]>l1[j+1]: 
            f=l1[j]              #Error
            l1[j]=l1[j+1]
            l1[j+1]=f
        c+=1
print(l1,c)
# print(l2)
# for i in range(len(l2)-1):
#     for j in range(len(l2)-1):
#         if l2[j]>l2[j+1]:
#             l2[j],l2[j+1]=l2[j+1],l2[j]
# print(l2)

