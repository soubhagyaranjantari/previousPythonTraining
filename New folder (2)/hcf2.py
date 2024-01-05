a=int(input('A:'))
b=int(input('B:'))
if a>0 and b>0:
    c=0
    for i in range(b,0,-1):
        if b%i==0 and a%i==0:
            
            break
    print(i)
else:
    print('Enter a number >0')