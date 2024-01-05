s='string'
def par(n):
    a,b,c='','',''
    for i in range(len(s)):
        if s[i]==n:
            index=i
            break
    a=s[:index]
    b=n
    c=s[index+1:]
    return a,b,c
# print(par(input()))
print(s.center(10,'*'))

