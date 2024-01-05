s='Soubhagya Ranjan Tarai'
print(s[::-1])
s1=''
for i in s:
    s1=i+s1
print(s1)
for i in range(len(s)-1,-1,-1):
    print(s[i],end='')
l=['1234','12345','12345']
l2=[]
for i in l:
    if type(i)==str:
        s1=''
        for z in i:
            s1=z+s1
        l2.append(str(s1))
print(l2)