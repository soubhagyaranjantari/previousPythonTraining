n=5
val=ord('A')
for i in range(n):
    for j in range(n):
        if i+j<=n-1 and i>=j:
            print(chr(val),end='')
            val+=1
            if ord('Z')> ord('Z'):
                val=ord('A')
        else:
            break
    print()   