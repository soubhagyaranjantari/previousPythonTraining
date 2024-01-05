a=55
b=75
for i in range(1,a*b+1):
    if i%a==0 and i%b==0:
        print(i)
        break