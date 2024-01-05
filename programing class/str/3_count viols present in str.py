s='ironman'
c=0
l=0
if "a"or"e"or"i"or"o"or"u" in s:
    print(True)
for i in s:
    if i== "a"or i=="e"or i=="i"or i=="o"or i=="u" in s:
        c+=1
print(c)
v='AEIOUaeiou'
for j in s:
    if j in v:
        l+=1
print(l)