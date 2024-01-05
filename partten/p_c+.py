a=int(input('row: '))
b=int(input('col: '))
c=1
for i in range(1,a+1):
    for j in range(1,b+1):
        print(c,end=' ')
       
    print()
    c+=1
    if c>9:
        c=1
   
   