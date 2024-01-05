n=int(input('N:'))
octa=0
i=0
while  n>0:
    rem=n%8
    octa=octa+rem*10**i
    n=n//8
    i=i+1
    
print(octa)

print(oct(100))