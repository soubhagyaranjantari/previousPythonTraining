# # # n=5
# # # for i in range(n):
# # #     for j in range(i+1):
# # #         print('*',end=' ')
# # #     print()

# # n=5
# # for i in range(n):
# #     for j in range(i,n):
# #         print("*",end=' ')
# #     print()
# # for i in range(n):
#     # for j in range(i+1):
#     #     print(' ',end=' ')
#     # for j in range(i,n):
#     #     print("*",end=' ')
#     # print()
# n=5
# # for i in range(n):
# #     for j in range(i,n):
# #         print(' ',end=' ')
# #     for j in range(i):
# #         print("*",end=' ')
# #     for j in range(i+1):
# #         print('*',end=' ')
# #     print()
# # n=5
# # for i in range(n):
# #     for j in range(i+1):
# #         print(' ',end=' ')
# #     for j in range(i,n-1):
# #         print("*",end=' ')
# #     for j in range(i,n):
# #         print("*",end=' ')
# #     print()

# # n=5
# # for i in range(n-1):
# #     for j in range(i,n):
# #         print(' ',end=' ')
# #     for j in range(i+1):
# #         print("*",end=' ')
# #     for j in range(i):
# #         print("*",end=' ')
# #     print()
# # for i in range(n):
# #     for j in range(i+1):
# #         print(" ",end=' ')
# #     for j in range(i,n):
# #         print('*',end=' ')
# #     for j in range(i,n-1):
# #         print("*",end=' ')
# #     print()

# # n=5
# # for i in range(n):
# #     for j in range(n):
# #         if i==j:
# #             print("*",end=' ')
# #         else:
# #             print(' ',end=' ')
# #     print()


# # for i in range(n):
# #     for j in range(n):
# #         if i+j==n-1 or i==j:
# #             print("*",end=' ')
# #         else:
# #             print(' ',end=' ')
# #     print()



# for i in range(n):
#     for j in range(n):      
#         if i>=j and i+j<=n-1:
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()
 

n=5
for i in range(n):
    for j in range(n):
        if j>=i and i+j>=n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()