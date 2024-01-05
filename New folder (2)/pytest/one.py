n=3
for i in range(n-1):
    for j in range(i,n):
        print(' ',end=' ')
    if i==0 and j==2:
        print('h',end=' ')
    for j in range(i+1):
        if i==1 and j==1:
            print('e',end=' ')
        else:
            print('*',end=' ')
    for j in range(i):       
        print('*',end=' ')    
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    
    for j in range(i,n):
        if i==0 and j==2:
            print('l',end=' ')
        if i==1 and j==2:
            print('l',end=' ')
        if i==2 and j==2:
            print('o',end=' ')
        else:
            print('*',end=' ')
        
        
    for j in range(i,n-2):
        print('*',end=' ')

       
    print()
    

