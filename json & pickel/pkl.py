import pickle as p
# l1=[1,2,3,4,5,6,7,8,9,0]
# with open ('pkl.pkl','wb+') as f:
#     p.dump(l1, f)
with open('pkl.pkl','rb+') as f:
    # l1=f.read()
    l1=p.load(f)
    print(l1)
    print(type(l1))