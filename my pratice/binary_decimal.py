n=int(input('N:'))
dec=0
i=0
while n>0:
    rem=n%8
    dec=dec+rem*10**i
    i+=1
    n//=8
print(dec)