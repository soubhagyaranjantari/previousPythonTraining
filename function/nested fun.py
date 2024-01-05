def one():
    print('one')
    def two():
        print('i am in 1')
    def three():
        print('i am in 2') 
    two()    
    three()
    print('end')       
one() 
