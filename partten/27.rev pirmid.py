n=int(input('n:'))
for i in range(n):
    for j in range(n):
        if i<=j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for k in range(n):
        if i+k<n-1:
            print('*',end=' ')  
        else:
            print(' ',end=' ')           
    print()   