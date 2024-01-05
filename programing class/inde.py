n=5
v=ord('A')
for i in range (n):
    for j in range(n):
        if i+j==n-1 or i==j:
            print(chr(v),end=' ')
            v+=1
            if v>ord('E'):
                v=ord('A')
        else:
            print(' ',end=' ')
    print()