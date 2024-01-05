l1=[['python',95] ,['laude',93]]
l2=[]
for i in range(len(l1)-1):
    if type [i]==list:
        for j in i:
            if type[j]==int:
                if i>j:
                    l2.append(j)
                else:
                    if i<j:
                        l2.append(j)
print(l2)

