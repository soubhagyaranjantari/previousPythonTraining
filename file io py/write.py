l=[]
n=int(input('enter how many word u want:'))
for i in range(n):
    val=input('enter value to document:')
    l.append(val)
l1=[]
for i in l:
    i+'hello'
    l1.append(i)
print(l1)
s=''
# s.
# f=open('sample1.txt','a+')
f=open('sample1.txt','w+')
f.writelines(l1)
f.write('\n hello how r you')
g=f.readlines()
f.seek(0)
print(f.read(5))
print(f.tell())

f.close()
# f1=open("sample1.txt",'r')
# f2=(f1.read(5))
# print(f2)
