import random
g=random.randint(1,100)
print(g)
user=None
guess=0
while user!=g:
    user=int(input("Enter Number To Guess->"))
    guess+=1
    if user==g:
        print("You Gausess Gight Number")
    else:
        if(user>g):
            print(f"Enter Less than {user}")
        else:
            print(f"Enter Greater than {user}")
print(f"***** You Gausess {guess} Times To Choose Right Number *****")
# with open("High Score.txt", "r") as f:
#     hiscore = int(f.read())
# if(guess<hiscore):
#     print("You have just broken the high score!")
#     with open("High Score.txt", "w") as f:
#         f.write(str(guess))


