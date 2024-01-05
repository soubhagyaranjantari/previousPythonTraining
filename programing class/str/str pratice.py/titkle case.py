s='soubhagya Ranjan tarai'
s1=''
for i in range(len(s)):
    if i==0 or s[i-1]==' ':
        if ord('a')<=ord(s[i])<=ord('z'):
            c=ord(s[i])-32
            s1+=chr(c)
        else:
            s1+=s[i]
    else:
        s1+=s[i]    
print(s1)