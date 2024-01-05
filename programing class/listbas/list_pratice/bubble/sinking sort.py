l1=[5,1,3,11,10,-5,-1,0,-0,-111,1.1]
# print(l1)
# # for i in range(len(l1)):
# #     for j in range(len(l1)-1-i):
# #         if l1[j]>l1[j+1]:
# #             l1[j],l1[j+1]=l1[j+1],l1[j]
# # print(l1)


for i in range(1,len(l1)):
    ele=l1[i]
    j=i-1
    while j>=0 and ele < l1[j]:
        l1[j+1]=l1[j]
        j=j-1
    l1[j+1]=ele
print(l1)


# if print('Hallo'):
#     pass
# else:
#     print('Hii')