l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
# print(l1[3:-1])
# l1=list(map(lambda n:n+5,l1))
# print(l1)
l2 = ['1', '2', '3']
# l2 = list(map(complex, l2,))
# print(l2)
l3 = 'THIS IS A - GOOD BOY - AND HE - IS GOOD'
l4 = l3.split('-',2)
print(l4)
l3 = list(map(len, l4))
# print(l3)
a1 = [1, 2, 3, 6, 7,  9, 0]
a = list(map(lambda a, b: a+b, l1, a1))
print(a)
