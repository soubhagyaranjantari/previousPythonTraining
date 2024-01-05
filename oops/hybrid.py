from json.encoder import py_encode_basestring_ascii


class google:
    company='google'
    location='India'
    def __init__(self) -> None:
        self.work='developer'
        self.time=8.00
    def getDtails(self):
        print(f'Company is {self.company}\nWork as a{self.work}And\nTime of working{self.time}')

class emp(google):
    def __init__(self):
        super().__init__()
        self.name ='Kanhu'
        self.salary =30000
    def DetailsOfEmp(self):
        print(f'''company is {self.company}\nWork as a {self.work}And\nTime of working{self.time}\nName of employe is {self.name}\nSalary is {self.salary}''')

class manager(google):
    def __init__(self) -> None:
        google.__init__(self)
        self.mgr = ['one','two']
        self.salary=None
    def DetailsOfMgr(self):
        print(f'''company is {self.company}\nWork as a {self.work} And \nTime of working{self.time}\nName of Managers is {self.mgr}\nSalary is {self.salary}''')


 