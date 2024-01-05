s=input()
c=0
for i in range(len(s)):
    if s[i] in ' ':
        c+=1
        print(s[i],':',i)
print(c)
