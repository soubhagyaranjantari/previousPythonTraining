# from collections import namedtuple
# import pickle

# from pyparsing import Regex

# def pickle_test():
#     P = namedtuple("P", "one two three four")
#     my_list = []
#     abe = P("abraham", "lincoln", "vampire", "hunter")
#     my_list.append(abe)
#     with open('abe.pickle', 'wb') as f:
#         pickle.dump(abe, f)
    
# pickle_test()
from scipy import stats
rvs = stats.norm.rvs(loc = 5, scale = 10, size = (50,2))
print (stats.ttest_1samp(rvs,5.0))
print(12345)