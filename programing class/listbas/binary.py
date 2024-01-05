def bin_search(li,size,a):
    f=0
    i=0
    u=size-1
    while i<=u and f==0:
        mid=(i+u)//2
        if li[mid]==a:
            p=mid+1
            f=1
        if li[ mid]<a:
            i= mid+1
        if li[ mid]>a:
            u=mid-1
    if f==1:
        print('Found at',p)
    else:
        print('Not found')
    
if __name__=='__main__':
    n=int(input('Enter size of li:'))
    _a=[]
    for i in range(1,1+n):
        # a=int(input('Enter Element of li:'))
        _a.append(i)
a1=int(input('Enter no. to search:'))
_a.sort()
print(_a)
bin_search(_a,i,a1)

        

        
    