l1=[10,20,30,40,50,60,70,80,90]
n=int(input('N:'))
l2=[]
for i in range (len(l1)):
    if len(l1)<n:
        print('index out of range')
    else:
        print(l1[n])
        break

# wrong
