n=int(input('N:'))
octal=0
i=0
while n>0:
    rem=n%8
    octal+=rem*10**i
    i+=1
    n=n//8
print(octal)