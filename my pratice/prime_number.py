n=int(input('Enter a number to reverse-->'))
if n<=1:
    print('enter a number greater than 1')
else:
    for i in range(2,n):
        if n%i==0:
            print('This is not prime number')
            break
    else:
            print('This is prime number')
