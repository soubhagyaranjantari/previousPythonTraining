n=int(input('N: '))
c=0
if n>0 and n>1:
    for i in range(2, n):
        if n%i==0:
            c=1
else:
    print('enter a number >1')
if c==1:
    print('this is not a prime')
else :
    print('prime')

        



