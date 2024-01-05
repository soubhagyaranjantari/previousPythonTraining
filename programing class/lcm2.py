# a=int(input('A: '))
# b=int(input('B: '))
a=12
b=20
v=set()
v2=set()
v1=set()
for i in range(1,a):
    if a%i==0 :
        print(i,end=' ')
        v.add(i)
        print(v1)
print()

for j in range(1,b):
    if b%i==0 :
        print(j,end=' ')
        v2.add(j)
        print(v1&v2)



print(v1-v2)


# v3=1
# for j in (v):
#     v3=v3*j
# print(v3)
        
# print(v)