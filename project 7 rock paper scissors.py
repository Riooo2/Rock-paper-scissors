#start game
#computer picks from rock paper scissors
#the user is asked for their answer in rock paper scissors
#
#score is counted depending who won

import random

options = ["rock","paper","scissors"]

def main():
    playagain = "yes"
    user_wins = 0
    computer_wins = 0
    while playagain != "no":
        

        choice = random.randint(0,2)
        computer_choice = options[choice]
        print("the computer has picked")
        
        #get the user choice
        user_choice = input(f"whats your pick{options}? ")
        if user_choice not in options:
            print("input not in choices, game reset, try again")
            print(f"computer wins: {computer_wins}")
            print(f"user wins: {user_wins}")
            main()
            

        print(f"you picked: {user_choice}")
        print(f"computer picked: {computer_choice}")

        #checkwho won
        if user_choice == 'rock' and computer_choice == "scissors":
            print("you win!")
            user_wins +=1
        elif user_choice == 'paper' and computer_choice == "rock":
            print("you win!")
            user_wins +=1
        elif user_choice == 'scissors' and computer_choice == "paper":
            print("you win!")
            user_wins +=1
        elif user_choice == computer_choice:
            print("draw!")
        else:
            print("computer won! ")
            computer_wins +=1


        #play again?
        playagain = input("Do you wanna play again(yes/no)? ")
        if playagain == "no":
            print(f"computer wins: {computer_wins}")
            print(f"user wins: {user_wins}")
            print("Thanks for playing!")    
            quit()
        elif playagain != "yes":
            print("cannot identify, please only choose ('yes' and 'no') game shall continue")
            print(f"computer wins: {computer_wins}")
            print(f"user wins: {user_wins}")


def get_user_choice():
    user_choice = input("whats your pick(rock, paper, scissors)? ")
    
        
def startgame():
    print("Welcome to rock paper sciccors")
    play = input("Do you want to play(yes/no?) ")
    if play == 'yes':
        main()



startgame()


#pseudo: make it so the game does not reset when encountering errors 