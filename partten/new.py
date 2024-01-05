# n= int(input('n:'))
# v=ord('A')
# for i in range(n):
#     for j in range(n):
#         if i <=j:
#             print(chr(v),end=' ')
#             v+=1
#             if v> ord('Z'):
#                 v=ord('A')

#     print()   



# n=5
# v=1
# for i in range(n):
#     for j in range(n):
#         if i+j>=n-1:
#             print(v,end=' ')
#         else:
#             print(' ',end=' ')
        
#     print()
#     # v+=1
#     # if v>9:
#     #     v=1

n=5
v=1
for i in range(n):
    for jj in range(n):
        if i==j or i+j==n-1:
            print(v,end=' ')
            # v+=1
            if v >9:
                v=1
        else: 
            print(' ',end=' ')
    print()