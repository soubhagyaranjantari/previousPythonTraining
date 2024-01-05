# l1=[1,2,2,3,4,55,5,55,4,44,33,44,22,88,22]
# for i in range(len(l1)-2):
#     d=l1[i]
#     for j in range(len(l1)-1):
#         if d == l1[j]:
#             print(l1.remove(d))
            
#         break
# print(l1)
# from functools import reduce
# # how to remove duplicate element from list?
# a = [1, 1,11,11,22,33,44,22,33,44,55,66,77,77,55, 2, 3]
# l2=list(reduce(lambda x, y: x if y in x else x + [y], a, []))
# print(l2)
sam_list = [11, 15, 13, 16, 13, 15, 16, 11] 
print ("The list is: " + str(sam_list)) 

# to remove duplicated from list 
sam_list = list(set(sam_list)) 

# printing list after removal 
# ordering distorted
print ("The list after removing duplicates: " + str(sam_list)) 