e=input('Enter ur email id\n')
a=False
b=False
c=False
d=False
f=False
for i in e:
    if i in "@":
        a=(True)
    elif i in 'gmail':
        c=True
    elif i in ".":
        d=True
    elif i in "com":
        f=True
    else:
        b=(True)
if a and b and c and d and f and len(e)>=10:
    print('Valid')
else:
    print('invalid')