l1=[]
n=int(input('N:'))
def app(l1,ele):
    l1+=[ele]
    return l1
for i in range(n):
    app(l1,int(input()))
print(l1)