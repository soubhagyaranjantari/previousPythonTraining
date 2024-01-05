n=27
hexa=''
while n>0:
    rem=n%16
    if rem<10:
        rem=rem+48
    else:
        rem=rem+87
    hexa=chr(rem)+hexa
    n=n//16
print(hexa)
# print(hex(3))
# print(300%16)
# print(int('a', 16))
# print(int(0xA))
# print((97-11))


