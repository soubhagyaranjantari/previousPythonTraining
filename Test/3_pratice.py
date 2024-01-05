# # l1=[1,2,3,4,5,6,7,8,9,10]
# # for i in l1:
# #     if i%2==0:
# #         print(i)

# #     else:
# #         pass


# l=[1,2,3,4,5,6,7,8,9,10]
# l1=[]
# n=3
# for i in range(0,len(l),n):
#     l2=[]
#     for j in range(i,i+n):
#         if j <len(l):
#             l2.append(l[j])
#     l1.append(l2)
# print(l1)
"""Inserction sort"""
# l1=[111,12,30,14,5,61,77,83,39,110]
# for i in range(1,len(l1)-1):
#     ele=l1[i]
#     j=i-1
#     while j>=0 and ele<l1[j]:
#         l1[j+1]=l1[j]

#         j=j-1
#     l1[j+1]=ele
# print(l1)




l1=[111,12,30,14,5,61,77,83,39,110]
for i in range(len(l1)-1):
    mip=i
    for j in range(i,len(l1)):
        if l1[mip] > l1[j]:
            mip=j

    temp=l1[i]
    l1[i]=l1[mip]
    l1[mip]=temp
print(l1)

