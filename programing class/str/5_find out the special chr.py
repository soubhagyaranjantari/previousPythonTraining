s="djkdasdQ!#🤣(●'◡'●)n$#!^_%&*&"
s1=0
for i in s:
    if (ord(i)in range(ord('a'),ord('z')+1)) or (ord(i) in range (ord('A'),ord('Z')+1)):
            if i in 'AEIOUaeiou':
                # v=v+1
                pass
            else:
                # c=c+1
                pass
    else:
        s1=s1+1

    
print(s1)
