n=int(input('n: '))
v=1
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')  
    for j in range(i+1):
        print(v,end=' ')
        v+=1
        if v >9:
            v=1   
    for j in range(i):
        print(v,end=' ')
        v+=1
        if v >9:
            v=1 
    print()
    # v+=1
    # if v> 9:
    #     v=1
    