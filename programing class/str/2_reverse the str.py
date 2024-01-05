s='ironman'
for i in range (len(s)-1,-1,-1):
    print(s[i],end='')
    
# print(s[::-1])
r=''
for i in s:
    r=i+r
print(r)