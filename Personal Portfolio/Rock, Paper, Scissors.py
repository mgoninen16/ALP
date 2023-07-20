from random import randint

t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]

player = False

while player == False:
    player = input("Please Select Rock, Paper, or Scissors: ")
    if player == computer:
        print("Tie! Play Again!")
    elif player == "Rock":
        if computer == "Paper":
            print("You Lose! Paper covers Rock!")
        else:
            print("You Win! Rock breaks Scissors!")
    elif player == "Paper":
        if computer == "Scissors":
            print("You Lose! Scissors cuts Paper!")
        else:
            print("You Win! Paper covers Rock!")
    elif player == "Scissors":
        if computer == "Rock":
            print("You Lose! Rock breaks Scissors!")
        else:
            print("You Win! Scissors cuts Paper!")
    else:
        print("That's not a valid play! Check your spelling and try again.")
    
    player = False
    computer = t[randint(0,2)]




