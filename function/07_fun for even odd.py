n=int(input('n:'))
def even(n):
    if n%2==0:
        return True
    else:
        return False
s=even(n)   
if s == True:
    print(f'{n} is a even number') 
else:
    print(f'{n} is odd number')    
    