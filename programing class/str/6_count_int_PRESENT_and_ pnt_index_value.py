s='spider1 spider9 spider3'
no="0123456789"
for i in range(len(s)):
    if s[i]in no:
        d=dict.fromkeys(s[i],i)
        print(d,end='')
