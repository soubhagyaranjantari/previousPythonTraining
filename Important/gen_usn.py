def usn(clg,yoj,branch):
    usn=1
    while (True):
        yield clg+str(yoj)+branch+str(usn)
        usn+=1
f=usn("An",2014,"EEE")
print(dir(f))
for i in range (50):
    print(next(f))