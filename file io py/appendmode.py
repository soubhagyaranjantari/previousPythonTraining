f=open('sample2.txt','a+')
f.seek(0)
a=f.read()
f1=open('sample3.txt','a+')
# f1.seek(0)
# f1.write(a.casefold())
f1.write(a.upper())
f1.seek(0)
f2=f1.read()
print(f2)
f.close()
f1.close()