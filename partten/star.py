n=int(input('n: '))
v=1
for i in range(n):
    for j in range(n):
        if i+j<=n-1 and i>=j:
          print('*',end=' ')
    print() 
    v+=1
    if v > 9:
        v=1
