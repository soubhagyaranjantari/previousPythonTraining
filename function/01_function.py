def pnt():
    print('hello how are you')
    print('good day sir')
def even():
    print('may i help to find even and odd number')    
    
   
    
n=int(input('enter a no\n')) 
even()
if n<0:
    print('enter a no "0" to avove')   
else:
    if n%2==0:
        pnt()
        print(f'{n} is a even number')    
    else:
        print(f'{n} is a odd number')    