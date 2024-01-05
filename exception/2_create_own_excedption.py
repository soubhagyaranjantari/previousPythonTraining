class age_greater_than40(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self) -> str:
        return self.msg
class age_less_21(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self) -> str:
        return self.msg
while (True):
    try:
        n=(input('Enter u r age:'))
        if n=='q':
            exit()
        n=int(n)
        if n>21:
            raise age_less_21("u r not twenty 1")
        elif n>40:
            raise age_greater_than40("u r above 40")
    except age_greater_than40 as e:
        print("u r not eligiable")
        print(e)
    except age_less_21 as e: 
        print('u r not 21')
        print(e)
    else:
        print("u r eligiable")

