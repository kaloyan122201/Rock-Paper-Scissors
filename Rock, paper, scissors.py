# Rock, paper, scissors game 

import random
# array with the options
options = ("Rock","Paper","Scissors")

#Create a bool varible which will help us if the player wants to play again without closing the program
#if the player won't play again --> playing = False and break the loop
playing = True

print("Let's play Rock, paper, scissors. There is 33.3%"," for you to win....or not!")
print("Ready?")

#keep looping until the player doesn't want to play again then --> playing = False
while playing:
    #Random option
    #We put it inside the loop so every time it iterates to pick a new desicion
    random_choice = random.choice(options)

    #We just create "our" variable as None ,we still haven't seen what the computer has chosen
    user_choice = None  
    
    #While you dont choose between R/P/S you are going to be asked the same question
    #If you play correctly you skip this loop
    while user_choice not in options :
        user_choice = input("Choose (Rock,Paper,Scissors): ")
    # We print what the user choose
    print("_________________________________________")    
    print("You choose:",user_choice.capitalize()) 

    # We print what the random choice from the computer and then we start with comparing  
    print("Computer chose:", random_choice)
    if user_choice == random_choice:
        print("It's a tie! ")
    elif user_choice == user_choice == "Rock" and random_choice == "Scissors": 
        print("You win!")
    elif user_choice == "Scissors"  and random_choice == "Paper":
        print("You win!")
    elif user_choice == "Paper" and random_choice == "Rock":
        print("You win!")
    #If we dont have a "Tie" or a "Win" then automatically its a "Lose"
    else:
        print("You lose!")

    #We ask if the user wants to play again  y/n
    play_again = input(("Want to play again? (y/n)")).lower()
    
    #depending on the answer we can change the playing varible we created in the beginning
    if not play_again == "y":
        playing = False
#Final message
print("Thanks for playing!")
