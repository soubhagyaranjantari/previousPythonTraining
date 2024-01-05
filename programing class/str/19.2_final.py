class rep:
    def __init__(self,s):
        self.s=s        
    def rep_place(self,old,new):
        s1=self.s
        s4=len(s1)+len(new)
        s5='Flase'
        s6=s1+new
        # print(s6)
        if old in s1:
            for a in range(len(old)):
                # pass
                S=''
                S+=old[a]
            # print(S)
                for i in range(len(s1)):
                        if s1[i]==old[0]: 
                            print(i)
                            # print('one')
                            for A in range(len(s1)):
                                if s1[A]==S:
                                    print(A)
                                    print('two')
                                    if i<=2:
                                        print(s1[:i]+new+s1[i+1:])
                                    elif i>=7:
                                        print(s1[:i]+new+s1[i+1:])
                                    elif i>=2:
                                        print(s1[:i-1]+new+s1[i+1:])
                                    elif i>=10:
                                        print(s1[:i]+new+s1[12:]+s1[-3:])
                        # for z in range(len(old)):
                        #     if  s1[z]==old[-1]:
                        #      print(z)
                        #      for e in range (len(s6)):
                        #          if s1[i]==old[0] and s1[z]==old[-1]:
                        #              print(True)
                        #              print((s1[:i]+new+s1[z+1:]))
                        # for e in range (len(s6)):
                        #     if s1[e]==old[0]:
                        #         print(e)
                        #         if i==e:
                        #             s5=(s1[:e-1])
                        #             if s6[e]==:
                        #                 s9=s1[e+1:]
                        #             s7=s5+new+s9

            #                         aaa=0
            #                         aaa=e
            
            #                         print(s7,len(s5))
            #                         # break
            # # print(j)
            # print(aaa)


        else:
            return (f'{old} word not in str')
s=rep(input())
(s.rep_place(input(),input()))
