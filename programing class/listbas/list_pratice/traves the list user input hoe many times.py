n=int(input('how many times u want'))
l1=[10,20,30,40,50]
for i in range(n):
    f=l1[0]
    for j in range(len(l1)-1):
        l1[j]=l1[j+1]
    l1[len(l1)-1]=f   
print(l1) 
# print(n%len(l1))