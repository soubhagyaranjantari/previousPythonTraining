def decorator(n):
    def find_out(n1):
        print("To check the number is odd  or even")
        n(n1)
        # print(f"{n1%2==0} is a even number:")
    return find_out
@decorator
def even_odd(a):
    if a%2==0:
        print(True)
    else:
        print(False)
even_odd(int(input("Enter a number:")))
