import json as j
# with open('file1.json') as f:
#     a=json.load(f,)
# print(type(a))
# print(a)
# s={'name':'soubhagya','loc':'odisha','a':True}
# j=json.dumps(s)
# # print(type(j))
# print((j))
# with open('file.json','r') as f:
#     # f.write(j)
#     # print(f.seek(0))
#     d=(f.read())
#     print(type(d))
f= open('file.json','r') 
d1=j.load(f)
# print(d1)
