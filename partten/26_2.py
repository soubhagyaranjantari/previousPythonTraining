# n=int(input('n:'))
# for i in range(n):
#     for j in range(n):
#         if j+i==n-1 and i==j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ') 
#     print()   



n=int(input('n:'))
for i in range(n):
    for j in range(n):
        if j+i>=n-1:
            print('*',end='\ ')
        else:
            print(' ',end=' |')
    for k in range(n):
        if i>k:
            print('*',end=' /')  
        else:
            print('8',end=' ,')           
    print()        
