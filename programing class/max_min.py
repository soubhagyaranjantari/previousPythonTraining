# n=9786542108
# j=[]
# while n>0:
#     a=n%10
#     j.append(a)
#     n//=10 
# print(j)
# print(j.sort())
# print(j[0],j[-1])
n=546781230
min=9
max=0
while n>0:
    rem=n%10
    if min>rem:
        min=rem 
    if max<rem:
        max=rem 
    n//=10
print(max,min)