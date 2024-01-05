import json
s='''
{
    "name" : "Soubhagya",
    "loc" : "Odisha"
}
'''
d=json.loads(s)
print(d['loc'])
d1={
    "name":"soubhagya",
    "loc": "Odisha"
}
d11=json.dumps(d1)
print(d11.split())