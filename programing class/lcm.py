a=int(input('A: '))
b=int(input('B: '))
# a=12
# b=18
c=1
s1=set()
for i in range(2,b):
    if a%i==0 or  b%i==0 :
        # print(i)
        # c=c*i
        s1.add(i)
print(s1)
#         for i in range(1,b):
#             if b%i==0 :
#                 print(i)
#                 c=c*i
# #         print(c)
# print('lcm is ',c)
        
        
        
