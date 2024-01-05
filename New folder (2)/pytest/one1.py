n=3
for i in range(n-1):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print ('*',end=' ')
    for j in range(i+1):
        print ('*',end=' ')
   
    print('h',end=' ')
    print('e',end=' ')
    print('l',end=' ')
    print('l',end=' ')
    print('o',end=' ')

  
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n-1):
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()

    