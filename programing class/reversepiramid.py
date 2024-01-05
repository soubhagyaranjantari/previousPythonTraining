n = int(input("N: "))
v = 9
for i in range(n-1):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i + 1):
        print(v, end=" ")
        v += 1
        if v > 9:
            v = 1
    for j in range(i):
        print(v, end=" ")
        v += 1
        if v > 9:
            v = 1
    print()
for i in range(n-1):
    for j in range(i + 1):
        print(" ", end=" ")
    for j in range(i, n):
        print(v, end=" ")
        v -= 1
        if v < 0:
            v = 9
    for j in range(i, n - 1):
        print(v, end=" ")
        v -= 1
        if v < 0:
            v = 9
    print()
    v = 9
