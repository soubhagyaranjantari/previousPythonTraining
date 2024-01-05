n=int(input("n= "))
hexa=' '
while n>0:
    rem=n%16
    if rem<10:
        rem=rem+48
    else:
        rem=rem+55
    n//=16
    hexa=chr(rem)+hexa
print(hexa)
print(hex(55))