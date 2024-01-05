n=int(input('enter a number: '))
def prime(n):
    if n<=1:
        print("entered number is not prime")
    else:
        for i in range(2,n):
            if n%i==0:
                print('entered number is not prime')
                break
        else:
                print("entered number is prime")        

prime(n)


