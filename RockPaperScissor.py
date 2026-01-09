import random

choices =["rock","paper","scissors"]

def RPS(choice):
    computer_choice = random.choice(choices)
    
    print("your choice: ", choice)
    print("computer choice ",choice)
    
    if choice == computer_choice:
        print("its a tie")
        return 0
    elif (choice == "rock" and computer_choice == "scissors") or \
         (choice == "paper" and computer_choice == "rock") or \
         (choice == "scissors" and computer_choice == "paper"):
        print("You won!")
        return 1 
    else:
        print("computer wins!")
        return -1
        
player_score = 0
computer_score = 0

while abs(player_score - computer_score) < 3:
    choice =input("enter your choice: ")
    result = RPS(choice)
    if result == 1:
        player_score +=1
    if result == -1:
        computer_score +=1
        
    print("player_score",player_score)
    print("computer_score",computer_score)
if player_score > computer_score:
    print("congrats you have won!")
elif player_score <computer_score:
    print("HAHA computer wins!")
else:
    print("It's a Tie try both of you harder!!")
    
    
