class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.address = None
class linklist:
    def __init__(self) -> None:
        self.head = None

    def insert(self,ele):
        n1=Node(ele)
        if self.head:
            n=self.head
            while n.address:
                n=n.address
            n.address=n1
        else:
            n=n1
        newNode=Node(ele)
        if self.head !=None :
            temp=self.head
            while temp.address:
                temp=temp.address
            print(temp.address)

            temp.address=newNode
        else:
            self.head=newNode
            
    def di(self):
        n=self.head
        while n:
            print(n.val)
            n=n.address
        


l=linklist()
l.insert(5)
l.insert(5)
l.insert(5)
l.di()
