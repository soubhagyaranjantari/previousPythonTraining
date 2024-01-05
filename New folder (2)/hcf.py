a=180
b=192
c=[]
for i in range(1,b):
    if a%i==0 and b%i==0:
        # print (i)
        c.append(i)

p=c.pop()
print(p)

c[::-1]
l=c.pop()
print(l)


