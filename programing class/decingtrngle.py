n=15
v=ord('Z')
for i in range(n):
    for j in range(i,n):
        print(chr(v),end=' ')
        v-=1
    print()
    