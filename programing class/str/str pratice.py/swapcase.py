s='SoubHagya ranjan Tarai'
s1=''
for i in s:
    if ord('a')<=ord(i)<=ord('z'):
        c=ord(i)-32
        s1+=chr(c)
    
    else:
        s1+=i
        #swapcase
        '''
        else:
        if ord('A')<=ord(i)<=ord('Z'):
            c=ord(i)+32
            s1+=chr(c)
        '''
print(s1)
