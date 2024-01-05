l1=[1,2,3,4,5,5,6,10]
s='enter a number:'
n=int(input(s))
c=0
for i in l1:
    if i==n:
        c+=1
print(c)