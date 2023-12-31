# Rock Paper Scissor:

import random


def gameWin(comp, you):
    # If Two Outputs are Equal then Declare a Tie!
    if comp == you:
        return None

    # Check For All Possibilities When Computer Choose 'r':
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True

    # Check For All Possibilities When Computer Choose 'p':
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    
    # Check For All Possibilities When Computer Choose 's':
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True

print("Comp Turn: Rock(r) Paper(p) Scissor(s)?")
randNo = random.randint (1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your Turn: Rock(r) Paper(p) or Scissor(s)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")

    

