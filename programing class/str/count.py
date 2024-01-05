s='catsasdogklscatjkjkljddog'
print(len(s))
c=0
d=0
for i in range(len(s)-2):
    if s[i]=='c' and s[i+1]=='a' and s[i+2]=='t':
        c+=1
    if s[i]=='d' and s[i+1]=='o' and s[i+2]=='g':
        d+=1
if c==d:
    print(True)
else:
    print(False)