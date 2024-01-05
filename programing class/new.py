n=5
v=ord("A")
for i in range(n):
    for j in range(n):
        if i>=j and i+j<=n-1:
            print(chr(v),end=' ')
            # v+=1
        else:
            break
    print()
    v+=1