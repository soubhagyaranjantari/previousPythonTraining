from hybrid import emp
from hybrid import manager
class person(emp,manager):
    def __init__(self):
        emp.__init__(self)
        manager.__init__(self)
        self.address = None
        self.age = None
    def DetailsOfMrg_profile(self):
        print(f'''company is {self.company}\nWork as a {self.work} And \nTime of working{self.time}\n
Name of Managers is {self.mgr}\nSalary is {self.salary}\nAdress of person{self.address}\nAge of person is {self.age}''')
    def DetailsOfEmp_Profile(self):
         print(f'''company is {self.company}\nWork as a {self.work}And\nTime of working{self.time}\nName of employe is {self.name}\nSalary is {self.salary}\n
 Adress of person{self.address}\nAge of person is {self.age}''')
        
p=person()
p.DetailsOfEmp_Profile()

