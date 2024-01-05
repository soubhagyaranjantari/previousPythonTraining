s='Soubhagya'
print(s)
def par(n):
    a,b,c='','',''
    for i in range(len(s)):
        if s[i]==n:
            ind=i
            break
    a=s[:ind]
    b=s[ind]
    c=s[ind+1:]
    return a,b,c
p=par('h')
print(p)
