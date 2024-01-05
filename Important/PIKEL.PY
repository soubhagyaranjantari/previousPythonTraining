import pickle
# car=['AUDI','BMW','MERCIDEZ']
# file="Mycar.pkl"
# fi_obj= open(file,'wb+')
# pickle.dump(car,fi_obj)
# fi_obj.close()

file="Mycar.pkl"
with open(file,"rb+") as f:
    mycar=pickle.load(f)
print(mycar)
# f=open(file,'rb')
# mycar=pickle.load(f)
# print(mycar)