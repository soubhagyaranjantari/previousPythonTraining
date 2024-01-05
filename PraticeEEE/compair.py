array1='142395687'
array2='12345689'
check=False
for i in array1:
    for j in array2:
        if i == j:
            check=True
            break
        else:
            check = False
print(check)