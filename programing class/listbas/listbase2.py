l1=[1,2,3,5,56,6,6,44,4,4443,23,44444,4,0]
e=0
o=0

for i in l1:
    if i%2==0:
        e+=1
    else:
        o+=1
print(e,'     ',o)