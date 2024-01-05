l1=[1,20,4,4,4,4,4,4,4,4,4,44,3,4,5,6,7,8,9]
p=-1
def search(a,n):
    """Find element in list"""
    for i in range(len(a)):
        if a[i]==n:
            global p
            p=i +1
            print('Found at position->',p)
            break
    else:
        print('element not found')
    
liner=search(l1,int(input('n:')))