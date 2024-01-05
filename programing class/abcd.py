n=5
v=ord('E')
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i+1):
        print(chr(v),end=' ')
        v+=1
        if v>ord('Z'):
            v=ord('A')
        
    print()