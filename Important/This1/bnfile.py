import pickle as pkl
l1=[1,2,3,4,5,6]
with open('file1.pkl','wb+') as f:
    pkl.dump(l1,f)

with open('file1.pkl','rb+') as f:
    l2=pkl.load(f)
print(l2)



# t=(i for i in range(10))
# print(type(t))
# print(dir(t))
# print(t.__next__())
# print(t.__next__())
# print(t.__next__())
# print(t.__next__())
# print(t.__next__())
# print(t.__next__())
# print(t.__next__())
# print(t.__next__())
# print(t.__next__())
# print(t.__next__())

# d1={
#     "name":'soubhagya'
# }
# print(d1)
# s=(str(d1))
# print(type(s))
# print(s)



# print(5 is 5)
