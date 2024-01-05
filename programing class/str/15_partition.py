s=input()
key=input()
new=''
for i in range(len(s)):
    if s[i] in key:
        if s[i]==key:
            new[i:s[i]:]
print(new)

