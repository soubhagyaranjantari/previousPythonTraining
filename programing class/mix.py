n=5 
v=1
for i in range(n):
    for j in range(n):
        if i==j or i+j == n-1:
            print(v,end="")
            v+=1
            if v> 5:
                v=1
        else:
            print(' ',end=' ')
    print()