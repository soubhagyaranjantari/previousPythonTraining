# n=5
# for i in range(n-1):
#     for j in range(i+1):
#         print("*",end=' ')
#     print()    
# for i in range(n):
#     for j in range(i,n):
#         print('*',end=' ')    
#     print() 

n=5
for i in range(n):
    for j in range(n):
        if i+j<=n-1 and i>=j:
            print('*',end='')
        else:
            break
    print()   