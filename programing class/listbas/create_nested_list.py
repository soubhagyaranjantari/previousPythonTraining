l1=[1,2,3,4,5,6,7,8,9,10,12,13,14]
n=int(input('n:'))
l2=[]
for i in range(0,len(l1),n):
    l2+=[l1[i:i+n]]
print(l2)