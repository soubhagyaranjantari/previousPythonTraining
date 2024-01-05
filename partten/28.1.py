n=5
val= n*2-1
for i in range(n):
    for k in range(i):
        print(' ',end=' ')
    for j in range(val):
        
        print('*',end=' ')
    print()
    val-=2


