# Rock, paper, scissors game 
# shte imame 3 opcii Rock, paper, scissors i vsqka ot tqh shte gi vkarame v if 
import random
# array s opcii
# izpolzvame tuple zashtoto nqma da promenqme stoinostite vutre te sa constanti
options = ("Rock","Paper","Scissors")



#suzdavame bool- koito shte ni pomogne ako user-a iska da igrae pak bez close the program!
#ako user-a ne iska da igrae otnovo slagame playing = false i taka escape-va loopa
playing = True

print("Let's play Rock, paper, scissors. There is 33.3%"," for you to win....or not!")
print("Ready?")

#dokato bool = true loopa shte vurti ako user-a kaje che ne iska da igrae pak --> playing = False
while playing:
    #random opciq v variable
    # slagame go v loop-a za da moje vseki put da izbere nova opciq
    random_choice = random.choice(options)

    #slagame izbora na user-a kato None za da moje da ne go suzdavame sled tova - pomaga za sega
    #slagame go loop-a za da moje da se reset-ne na vseki cikul
    user_choice = None # samo go suzdavame bez stoinost 
    
    
    # dokato izbora ne e v options loop-a shte produljava , ako izbere R/P/S preskacha 
    #avtomatichno user_choice vliza vutre zashtoto e ravno na None vij line 10
    while user_choice not in options :
        user_choice = input("Choose (Rock,Paper,Scissors): ")
        
    print("_________________________________________")    
    print("You choose:",user_choice.capitalize()) 

    # po tozi nachin dori i 10 puti da napisha !=R/P/S posle izliza print    
    print("Computer chose:", random_choice)
    if user_choice == random_choice:
        print("It's a tie! ")
    elif user_choice == user_choice == "Rock" and random_choice == "Scissors": 
        print("You win!")
    elif user_choice == "Scissors"  and random_choice == "Paper":
        print("You win!")
    elif user_choice == "Paper" and random_choice == "Rock":
        print("You win!")
    #Ako nqma ravenstvo ili ne sreshtame win condition - avtomatichno oznachava che gubim!!!!!
    else:
        print("You lose!")
        
    play_again = input(("Want to play again? (y/n)")).lower()# ako sluchaino napishe "Y" ili "N" vmesto "y" i "n"
    
    #ako user-a ne iska da igrae otnovo(y) , escape the loop
    if not play_again == "y":
        playing = False
#Kogato izleznem ot loop-a
print("Thanks for playing!")