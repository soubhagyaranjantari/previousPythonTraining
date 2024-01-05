import pickle as pkl
s={'name':'soubhagya','loc':'odisha','a':'True'}
with open ("file3.pkl",'wb+') as f:
    pkl.dump(s,f)

with open("file3.pkl","rb+") as f:
    d1=pkl.load(f)
with open('file5.txt','w+') as d:
    d.write(str(d1))
print(d1)