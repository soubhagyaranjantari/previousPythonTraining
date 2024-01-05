s='spiderman'
a='spider'
b='iron'
c=''
if a in s:
    c+=b
print(c+s)

for i in range(len(s)):
    if s[i:len(s)]==a:
        b=s[len(a):]
print(b)
