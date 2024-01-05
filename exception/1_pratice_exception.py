while True:
    try:
        s={'add','mul','div','sub'}
        a=(input('Enter a number1:'))
        if a=='q':
            exit()
            break
        a=float(a)
        b=float(input('Enter a number2:'))
        n=input(f'Option are {(s)}\n')
        if n=='add':
            c=a+b
            print(c)
        elif n=='sub':
            c=a-b
            print(c)
        elif n=='mul':
            c=a*b
            print(c)
        else:
            c=a/b
            print(c)
    except Exception as e:
        print(e)
    else:
        print('try statement is sucessful run')
    finally:
        print('we r sucessful to run the programme')
print('u r sucessful')