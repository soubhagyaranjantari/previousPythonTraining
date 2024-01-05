# l1=[-1,1,2,3,4,4,4,4,5,6,7,8,9,]
# n=int(input(";enter a number to search:"))  #5<8
# f=l1[0]
# l=l1[-1]
# print(f,   l)
# while f<=l:
#     m=(f+l)//2
#     if l1[m]<n:
#         f=m+1
#     elif l1[m]>n:
#         l=m-1
#     else:
#         print(True,'FOUND AT :',m)
#         break
# else:
#     print(False)        


# l1=[1,2,3,4,7,8,99,111]
# n=int(input(    ))
# f=0
# last=len(l1)-1
# while f < last:
#     mid=(f+last)//2
#     if l1[mid] > n:
#         last=mid-1
#     elif l1[mid] <n:
#         f= mid +1
#     else:
#         print("ele found at",mid+1)
#         break
# else:
#     print("ele not found")

l1=[1,2,3,-5,88,77,33,111,132,14]
# for i in range(len(l1)):
#     for j in range(len(l1)-1-i):
#         if l1[j]>l1[j+1]:
#             l1[j+1],l1[j]=l1[j],l1[j+1]
print(l1)
for i in range(1,len(l1)):
    ele=l1[i]
    j=i-1
    while j>=0 and ele <l1[j]:
        l1[j+1]=l1[j]
        j=j-1
    l1[j+1]=ele
print(l1)
#
# for i in range(1,len(l1)):
#     ele=l1[i]
#     j=i-1
#     while j>=0 and ele <l1[j]:
#         l1[j+1]=l1[j]
#         j=j-1
#     l1[j+1]=ele
# print(l1)