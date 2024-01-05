n=int(input("N:"))
# perfect=0
# for i in range(1,n):
#     if n%i==0:
#         perfect+=i
#         print(i)
# if perfect==n:
#     print(True)
# else:
#     print(False)
# strong=0
a=n
while n>0:
    fact=1

    rem=n%10
    for i in range(1,rem+1):
        fact=fact*i
        print(fact,end=' ')
#     strong=strong+fact
#     print(n,end=' ')
    n=n//10
#     print(strong)
#     # print(n)
# if a==strong:
#     print(True)
# else:
#     print(False)

# len=0
# armstrong=0
# while n>0:
#     rem=n%10
#     len+=1
#     n=n//10
# n=a
# while n>0:
#     rem=n%10
#     armstrong=armstrong+rem**len
#     n=n//10
# if armstrong==a:
#     print(True)
# else:
#     print(False)

# mul=1
# add=0
# while n>0:
#     rem=n%10
#     n//=10
#     break

# add=rem+n
# mul=rem*n
# if add+mul==a:
#     print(True)
# else:
#     print(False)