# # # # n=145
# # # # a=n
# # # # sum=0
# # # # while n>0:
# # # #     fact=1
# # # #     rem=n%10
# # # #     for i in range(1,rem+1):
# # # #         fact=fact*i
# # # #     print(fact)
# # # #     sum+=fact
# # # #     print(sum)
# # # #     n//=10
# # # # print(a==sum)
# # # # # print(sum)
# # # #@@@ perfectno
# # # n=6
# # # sum1=0
# # # for i in range(1,n):
# # #     if n%i==0:
# # #         sum1+=i
# # # print(sum1)
# # n=1009
# # s=0
# # m=1
# # while n>0:
# #     rem=n%10
# #     b=n//10
# #     break
# # print((rem+b)+(rem*b))
# d = {
#     '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0,
#     'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
# }
# n = input('N:').strip().lower()
# power = len(n)-1
# d1 = 0
# c=0
# for i in n:
#     d1 += d[i]*16**power
#     print(16**power)
#     power -= 1
#     c+=1
# 1
# print(d1)
# print(c)
l1='1,2,3,4,5'
print(l1.strip('3'))

# hex_to_dec_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10 , 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

# hex = input("Enter the hexadecimal number: ").strip().upper()
# dec = 0
# length = len(hex) -1

# for digit in hex:
#     dec += hex_to_dec_table[digit]*16**length
#     length -= 1

# print("Decimal value is : ",dec)
# # print(hex(283))
