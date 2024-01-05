s='soubHagya ranjan tarai'
v=0
c=0
sp=0
for i in s:
    if i in 'AEIOUaeiou':
        v+=1
    
    elif ord('a')<=ord(i)<=ord('z') or ord('A')<=ord(i)<=ord('Z'):
        c+=1
    else:
        sp+=1
print(v,c,sp)