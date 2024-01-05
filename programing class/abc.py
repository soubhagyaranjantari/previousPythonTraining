n=5
v=ord('Z')
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n):
        print(chr(v),end=' ')
        v-=1

    print()
    # v=ord('A')