
import random
RandNumber = random.randint(1,100)
UserGuess = None
Guesses = 0

while(UserGuess != RandNumber):
    UserGuess = int(input("Enter your guess: "))
    Guesses += 1
    if(UserGuess==RandNumber):
        print("You Guessed it Right!")
    else:
        if(UserGuess>RandNumber):
            print("You Guessed it wrong! Enter a smaller number")
        else:
            print("You Guessed it wrong! Enter a larger number")

print(f"You Guessed the Number in {Guesses} Guesses")
with open("HighScore.txt", "r") as f:
    HighScore= int(f.read())

if(Guesses<HighScore):
    print("You have just broken the High Score!")
    with open("HighScore.txt", "w") as f:
        f.write(str(Guesses))
