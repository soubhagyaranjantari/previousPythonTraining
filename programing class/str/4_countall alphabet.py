s="it's my class"
v=0
c=0
for i in s:
    if (ord(i)in range(ord('a'),ord('z')+1)) or (ord(i) in range (ord('A'),ord('Z')+1)):
        if i in 'AEIOUaeiou':
            v=v+1
        else:
            c=c+1
print(v,c)
print(ord('a'))

