class notes:
    def view(self):
        print('i am view method')
    def _test(self):
        print('i am test method')
        self.__diplsy() 
        print('i am  in nature') 
    def __diplsy(self):
        print('i am privete method')
n1=notes()
n1.view()
n1._test()
# n1.__diplsy()
import oops as o
o.x.bc