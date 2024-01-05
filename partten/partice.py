# r=int(input('rpw:'))
# c=int(input('col:'))
# v=1
# for i in range(1,r+1):
#     for j in range(1,c+1):
#         print(v,end=' ')
#         v+=1
#         if v>9:
#             v=1

#     print()
#     v=1

n=int(input('row: '))
c=int(input('col: '))
v=9
for i  in range(1,n+1):
    for j in range(1,c+1):
        print(v,end=' ')

    print()
    v-=1
    if v<1:
        v=9

