f=open('sample.txt','r+')
f.write('this a created file')
# f.write(' this a created file1\n')
# f.write(' this a created file2')
a=f.read()

print(a)
# print(f.readline())
# print(f.readline())
# print(f.readlines())
# if f.writable():
#     print (True)
# else:
#     print(False)
f.close()