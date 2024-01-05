# # # # # n=121
# # # # # rev=0
# # # # # # while n>0:
# # # # # #     rem=n%10
# # # # # #     rev=rev*10+rem
# # # # # #     n=n//10
# # # # # # print(rev)


# # # # # a=n
# # # # # while (n>0):
# # # # #     rem=n%10
# # # # #     rev=rev*10+rem
# # # # #     n//=10
# # # # # # print(rev)
# # # # # if a== rev :
# # # # #     print(True)
# # # # # else:
# # # # #     print(False)

# # # # '''decimal to binary'''
# # # # # n=20
# # # # # i=0
# # # # # bin=0
# # # # # while n>0:
# # # # #     rem=n%2
# # # # #     bin=bin+rem*10**i
# # # # #     i+=1
# # # # #     n//=2

# # # # # print(bin)

# # # # """bin to decimal"""
# # # # # n=111
# # # # # dec=0
# # # # # i=0
# # # # # while n>0:
# # # # #     rem=n%10
# # # # #     dec=dec+rem*2**i
# # # # #     i+=1
# # # # #     n//=10
# # # # # print(dec)


# # # # # n=500
# # # # # fib=0
# # # # # a=0
# # # # # b=1
# # # # # while n>fib:
# # # # #     fib=a+fib
# # # # #     a=b
# # # # #     b=a
# # # # #     print(fib,end=' ')
# # # # # a=0
# # # # # b=1
# # # # # c=0
# # # # # for i in range(10):
# # # # #     print(c,end=' ')
# # # # #     a=b
# # # # #     b=c
# # # # #     c=a+b
# # # # n=500
# # # # a, b,c = 0, 1,0
# # # # while c < n:
# # # #     print(c, end=' ')
# # # #     # a, b = b, a+b
# # # #     # a=b
# # # #     # b=a+b
# # # #     a=b
# # # #     b=c
# # # #     c=a+b



# # # hexa=''
# # # n=256
# # # while n>0:
# # #     rem=n%16

# # #     if rem<10:
# # #         rem=rem+48
# # #     else:
# # #         rem=rem+55
# # #     n//=16
# # #     hexa=chr(rem)+hexa
# # # print(hexa)
# # # print(hex(256))

# # # n=256
# # # oc=0
# # # i=0
# # # while n>0:
# # #     rem=n%8
# # #     oc=oc+rem*10**i
# # #     i+=1
# # #     n//=8
# # # print(oc)
# # # print(oct(256))

# # from tkinter import N


# # n=145
# # # a=n
# # add=5
# # while n>0:
# #     rem=n%10
# #     fact=1
# #     for i in range(1,rem+1):
# #         fact=fact*i
# #     add=add+fact
# #     n//=10
# #     # print(add)
# #     print(fact)
# n=20
# a=0
# for i in range(1,n):
#     if n%i==0:
#         a=a+i
# print(a)




n=119

while True:
    rem=n%10
    a=n//10
    if (rem+a) +(rem*a)==n:
        print(True)
    else:
        print(False)
    break

