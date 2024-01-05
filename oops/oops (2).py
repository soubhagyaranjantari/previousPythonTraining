class oops:
    a=50
    b=10
    def __init__(self):
        print(self)
        self.a=30
        self.d=20
    def prit(self)  :
        print('this a method')
        
# w=oops()
# w.prit()
# print(w)  
# print(w.a)
# print(oops.a)
# print(oops.a)
# x=oops()
# print(oops.a)

class clas_of_clan:
    troops1='valkery'
    troops2='pika'
    def war_attack(self):
        print('i am best')

def normal_mode():
    print('Normal attack')

normal_mode()

c=clas_of_clan()
print(type(c))
b=c.troops1
print(b)
c.war_attack()