a,b=10,20
c=max(a,b)
for i in range(10,c):
    for j in range(2,i):
        if i%j ==0:
            print('not prime',i)
            break
            
else:
    print('prime',i)