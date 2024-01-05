
n=12342357687907876523415278
min=9
max=0
while n>0:
    rem=n%10
    if min>rem:
        min=rem
    if max<rem:
        max=rem
    n=n//10
print(min,max)