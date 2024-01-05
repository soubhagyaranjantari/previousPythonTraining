n=int(input('n: '))
for i in range(n):
    for j in range(3):
        if j-i==j:
            print('*',end=' ')
    print()
    '''
    x
    xx
    xxx
    xx
    x
    '''