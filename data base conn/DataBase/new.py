# l1 = [1, 2, 3, [4, 5, 6, [7, 8, 9, 10] ] ]
# l1 = [1,[2,3,[4,5,6],7,[8,9]]]
l1 = [ 1, 2, [3, 4, 5], 6, [7, 8], [9]]
print(l1)

l2 = []

def newlist(l1):
    for i in l1:
        if type(i) == list:
            newlist(i)
        else:
            l2.append(i)

newlist(l1)
print("new list :->",l2)