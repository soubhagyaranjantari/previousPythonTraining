import numpy as np
import pandas as pd


d={
    'name':['kanhu','anil','soumya'],
    'age':[25,24,24],
    'city':['Odisha',"odisha","Odisha"]
}
n=pd.DataFrame(d)
# print(n)
# n.to_csv('frinds.csv')   to save in exel format
# n.to_csv('frinds1.csv',index=False)    to save in exel format without index
# print(n.describe())   ive the min to max value 

# n1=pd.read_csv('frinds.csv')   use to read data from exel shit
# print(n1)
# print(n1.head(2))   give the first 2 row
# print(n1.tail(2))   give the last 2 row
"""
to change the index value to anything 
n.index=['one','two','three']
"""