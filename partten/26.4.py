n=int(input('n: '))
val=ord('A')+n-1
for i in range(n):
    for j  in range(n-1-i):
        print(' ',end=' ')
    for k in range(2*i+1):
        val+=1
        if val > ord('Z'):
            val=ord('A')
        print(chr(val),end=' ')
    print()        



'''
strat with v same pro.
in reverse start z
9
'''