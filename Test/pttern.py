n=5
cap=ord("A")
sm=ord('a')
c=0
for i in range(n,):
    for j in range(n):
        if i==j or i+j==n+1:
            print(chr(cap+c),end=' ')
        else:
            print(chr(sm+c),end=' ')
            # print(" ",end=' ')
        c+=1
    print()