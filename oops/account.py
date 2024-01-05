class account:
    bank_name='axis'
    Ifsc=1234567890
    branch='Rajajinagar'
    def __init__(self,acc_no,acc_name,balance=123):
        self.acc_no=acc_no
        self.acc_name=acc_name
        self.balance=balance
    def imfo(self):
        print(f'Bank Name {self.bank_name}\n IFSC {self.Ifsc}\n Branch {self.branch}\n accno {self.acc_no}\n acc name {self.acc_name}\n balance {self.balance}')
        
a1=account(12345,'ANIL')
a1.imfo()