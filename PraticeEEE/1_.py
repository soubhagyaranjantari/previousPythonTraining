n=5
v=1
for i in range(n):
    v=1
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i+1):
        print(v,end=' ')
    for j in range(i):
        print(v,end=' ')
        v+=1
    print()