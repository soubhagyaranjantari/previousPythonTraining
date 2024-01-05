n=100
sum=0
perfect=[]
for i in range(1,n+1):
    for j in range(1,i):
        if i%j==0:
            sum=sum+j
            if sum==i:
                perfect.append(sum)
print(perfect)
        
#             sum=sum+j
#             perfect.append(sum)
# print(perfect)



