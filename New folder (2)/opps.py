from tkinter import N


class prinme:
    def __init__(self,n) -> None:
        self.n=n
        for i in range(2,n):
            if n%i==0:
                print('not prime')
                break
            else:
                print('prime')


p=prinme(int(input('N:')))