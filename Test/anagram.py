s1 = 'abcdec'
s2 = 'cdzeab'
a = False
if len(s1) == len(s2):
    c=0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                a = True
                break
        else:
            a = False
            break
else:
    a = False
if a:
    print('Amangram String')
else:
    print('Not Amangram String')
