class rep:
    def __init__(self,s):
        self.s=s        
    def rep_place(self,old,new):
        s1=self.s
        if old in s1:
            for i in range(len(s1)):
                if s1[i]==(old):
                    return (s1[:i]+new+s1[i+1:])
        else:
            return (f'{old} word not in str')
s=rep(input())
print (s.rep_place(input(),input()))
# s='This is a good way'
# print(s.replace('This','That'))