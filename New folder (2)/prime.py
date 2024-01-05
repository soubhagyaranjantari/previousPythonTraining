# # class function:

# #     def __init__(self,a):
# #         self.f = 1
# #         for j in range(1,a):
# #             f=j*f
# #         print(self.f)
    

# # f=function(int(input()))




# n=int(input('N:'))
# # f=1
# # for j in range(1,n+1):
# #     f=j*f
# # print(f)
# p=2
# while n >0:
#     for j in range(2,p):
#         if p%j==0:
#             break
#     else:
#         print(p,end=' ')
#         n=n-1
#     p+=1


l1=[1,33,2,44,333,22,11]
# for i in range(len(l1)-1):
#     for j in range(len(l1)-1-i):
#         if l1[j]>l1[j+1]:
#             l1[j],l1[j+1]=l1[j+1],l1[j]
print(l1)
for i in range(len(l1)-1):
    minv=i
    for j in range(i,len(l1)):
        if l1[minv]>l1[j]:
            minv=j
    l1[i],l1[minv]=l1[minv],l1[i]
print(l1)

