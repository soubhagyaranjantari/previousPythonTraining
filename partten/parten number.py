# n=int(input('n:'))
# for i in range(n):
#     print('*'*n)
    
    
    
r=int(input('row: '))
o=int(input('col: '))
b=1

for i in range(1,r+1):
    for j in range(o):
        print(b, end=" ")
    print() 
    b+=1
    if b>9:
        b=1  
