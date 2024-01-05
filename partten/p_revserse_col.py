
n = int(input('row: '))
c = int(input('col: '))
v = 9
for i in range(1,n+1):
    if i>9:
        i=9
    for j in range(1,c+1):
        print(v,' ',end=' ')
        v-=1
        if v<1:
            v=9
    print()    
    print()    
  
        
        
        
