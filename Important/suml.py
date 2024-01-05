n=1212200
a=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n//=10
print(rev)
# # # # n=123451122009866
# # # # e=0
# # # # o=0
# # # # while n>0:
# # # #     rem=n%10
# # # #     if rem!=0:
# # # #         if rem%2==0:
# # # #             e+=1
# # # #         else:
# # # #             o+=1
# # # #     n//=10
# # # # print(e,o)
# # # n=5
# # # a=0
# # # b=1
# # # c=0
# # # for i in range(n):
# # #     print(c,end=' ')
# # #     a=b
# # #     b=c
# # #     c=a+b
# # n=10
# # bi=0
# # i=0
# # while n>0:
# #     rem=n%2
# #     bi=bi+rem*10**i
# #     n//=2
# #     i+=1
# # print(bi)
# n=1010
# dec=0
# i=0
# while n>0:
#     rem=n%8
#     dec=dec+rem*10**i
#     i+=1
#     n//=8
# print(oct(1010))
# print(dec)
# n=30
# hexa=''
# while n>0:
#     rem=n%16
#     if rem<10:
#         rem=rem+48
#     else:
#         rem=rem+55
#     hexa=chr(rem)+hexa
#     n=n//16
# print(hexa)
# print(hex(30))

