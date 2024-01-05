def fact(n):
        fact=1
        fact1=fact1*fact(n-1)
        if n==1 or n==0:
            return fact1

print(fact(5))
    