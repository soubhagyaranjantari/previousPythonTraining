b = int(input('col:\n'))

c = 1

for i in range(1, (int(input('row:\n')))+1):

    for j in range(b):

        print(c, end=' ')

    print()

    c += 1

    if c > 9:

        c = 1
sum(i)