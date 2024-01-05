n=5
v=ord('E')
for i in range(n):
    for j in range(i,n):
        print(chr(v),end=' ')
        v+=1
        if v>ord('Z'):
            v=ord('A')

   
    print()
    # v=ord('A')