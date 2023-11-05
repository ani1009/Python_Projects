''' Write a Python Program Which Will Keep Adding a Stream Of Numbers Inputted By the User. 
The Adding Stops As Soon As User Presses 'q' Key On the Keyboard. '''

sum = 0
while(True):
    userInput = input(" 'Enter the Item Price' Or 'Press q to Quit' : \n ")
    if (userInput != 'q'):
        sum = sum + int(userInput)
        print(f" Your Order Total is : {sum} ")

    else:
        print(f" Your Bill Total is : {sum}. Thanks!")
        break
