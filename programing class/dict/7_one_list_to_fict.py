# l1=[1,2,3,4,5]
# d1={x:x**2 for x in l1}
# print(d1)
s=set()
# print(type(s))
s1={i**5 for i in range(5)}
print(s1)
s2=s1.remove(32)
print(s2)
print(s1)
