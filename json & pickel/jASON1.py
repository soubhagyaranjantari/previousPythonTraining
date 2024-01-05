import json as j
s={"name":"Soubhagya","loc":"Odisha","mob":9114084206,"any":True}
# d=j.loads(s)
# print(type(d))
# print((d))
with open('file.json','w+') as f:
    a=j.dump(s,f)
    print(a)
