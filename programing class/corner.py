n=5
v=ord('E')
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print(chr(v),end=' ')
            v+=1
            if v<ord('A'):
                v=ord('Z')
        else:
            print(" ",end=' ')
    print()