# # for i in range(2,n):
# #     if n%i==0:
# #         print("not")
# #         break
# # else:
# #     print("pri")
        
# # for i in range(2,n):
# #     if n%i==0:
# #         print(n,"not prime number")
# #         break
# # else:
# #     print(i,"is A PRIME NUMBER")

# n=int(input('enter the number >'))
# prime=2
# while n!=0:
#     for i in range(2,prime):
#         if prime%i==0:
#             prime+=1
#             break
#     else:
#         print(prime,end=" ")
#         n-=1
#         prime+=1














def prime(n):
    for i in range(2,n):
        if n%i==0:
            print("not")
            break
    else:
        print("prime")
# prime(10)


# def prime(n):
#     while n>0:


n=0
s='bhavesh'
while n !=50:
    n+=1
    print(s,n)
