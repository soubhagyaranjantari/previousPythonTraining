n=int(input('n:'))
val=ord('A')
for i in range(n):
    val=ord('A')
    for j in range(i+1):
        print(chr(val),end=' ')
        val+=1
        if val> ord('Z'):
            val=ord('A')
    print()


# n=int(input('n:'))
# for i in range(n):
#     for j in range(n):
#         if j+i==n-1 or i==j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ') 
#     print()        