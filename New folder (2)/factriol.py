n=int(input('N:'))
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)

f=fact(n)
print(f)


# factorial number?
fact = 1
num = int(input("enter the number"))
if num < 0:
   print("Enter a +ve number")
elif num == 0:
   print("0 factorial =1")
else:
   for i in range(1, num + 1):
       fact = fact * i
print("Factorial of", num, "=", fact)