'1. Local Scope----------------------------->'
# num=0
# def demo():
#     print(num)
#     num=1
#     print("The Number is:",num)
# demo()


"# 2. Global Scope--------------------------->"
# def demo():  
#     print(Str) 
#     Str = "You are smart"
#     print(Str) 
# # Global scope 
# Str = "You are Clever" 
# demo() 
# print(Str) 

"# 3. NonLocal or Enclosing Scope------------->"
# def func_outer():
#     x = "local"
#     def func_inner():
#         global x
#         x = "nonlocal"
#         print("inner:", x)
#     func_inner()
#     print("outer:", x)
# func_outer()





"4. Built-in Scope"
# Built-in Scope 
# from math import pi 
# # pi = 'Not defined in global pi'
# def func_outer(): 
#     # pi = 'Not defined in outer pi' 
#     def inner(): 
#         # pi = 'not defined in inner pi' 
#         print(pi) 
#     inner() 
# func_outer()









# def fib(n):
#      a, b = 0, 1
#      while a < n:
#          print(a, end=' ')
#          a, b = b, a+b
#      print()
# fib(1000)
'.........'
# print(0>-1)






'Selection sort'
l1=[5,2,3,1,9,0,-1,-5,5]
print(l1)
o=0
i1=0
ii=0
for i in range(0,len(l1)-1):
    min_value=i
    o+=1
    for j  in range(i,len(l1)):
        i1+=1
        # if l1[j] < l1[min_value]:
        if l1[min_value]> l1[j]:
            min_value=j
            ii+=1
    l1[i],l1[min_value]=l1[min_value],l1[i]
    # temp=l1[i]
    # l1[i]=l1[min_value]
    # l1[min_value]=temp
print(l1,'           ',o,i1,ii)

# l1=[False,0,5]
# l1=min(l1)

# print(l1)