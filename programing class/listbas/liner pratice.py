l=[1,2,3,4,5,6,7,8,9]
p=-1
n=int( input ('Enter a number:'))
for i in range(len(l)):
    if l[i]==n:
        p=i+1
        print(f'{n} found at positino',p)
        break
else:
    print('Element not found')