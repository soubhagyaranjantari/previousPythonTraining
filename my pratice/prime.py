# def fun(n):
# 	v=ord('E')
# 	for i in range(n):
# 		for j in range(i,n):
# 			print(chr(v),end=' ')
# 			v-=1
# 		print()
# fun(5)
v=ord('E')
v1=ord('I')
v2=ord('L')
v3=ord('N')
v4=ord('O')
n=5
for i in range(n):
	for j in range(i,n):
		if i==0:
			print(chr(v),end=' ')
			v-=1
		if i==1:
			print(chr(v1),end=' ')
			v1-=1
		if i==2:
			print(chr(v2),end=' ')
			v2-=1
		if i==3:
			print(chr(v3),end=' ')
			v3-=1
		if i==4:
			print(chr(v4),end=' ')
			v4-=1

	print()