a=int(input('Enter a number to reverse-->'))
b=int(input('Enter a number to reverse-->'))
if a>b:
    mx=a
else:
    mx=b

print(mx)
for i in range(mx,0,-1):
    if a%i==0 and b%i==0:
        print(i)
        break

      
