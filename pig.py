"""Pig game with Python"""

import random

def instructions():
    print("Game start to paly with computer.")
    print("Rules: Two palyers take turns; on each turn, a player rolls a six-sided die as many times as she wishes, or until she rolls a 1.\n Each number she rolls, except a 1, is added to her score this turn; but if she rolls a 1, her score for this turn is zero, and her turn ends. \nAt the end of each turn, the score for that turn is added to the player's total score. The first player to reach or exceed 100 wins.\n")

def current_score(computer_score, human_score):
    print("Computer score: ", computer_score)
    print("Human score: ", human_score)
    if computer_score > human_score:
        print("You are behind computer:", computer_score - human_score)
    else:
        print("You are ahead computer:", human_score - computer_score)

def human_move(computer_score, human_score):
    current_score(computer_score, human_score)
    total_roll = 0
    while ask_yes_or_no():
        this_roll = roll()
        if this_roll == 1:
            print("You are rolling 1. ")
            current_score(computer_score, 0)
            return 0
        else:
            total_roll = total_roll + this_roll
            print("You are rolling ", this_roll)
            current_score(computer_score, total_roll + human_score)

    return total_roll + human_score

def computer_move(computer_score, human_score):
    print("Computer is rolling.")
    total_roll = 0
    for i in range (1,4):
        this_roll = roll()
        if this_roll == 1:
            return 0
        else:
            total_roll = total_roll + this_roll

    return computer_score + total_roll

def roll():
    return random.randrange(1,7,1)

def ask_yes_or_no():
    again = input("Want to try again?(y/Y-yes,n/N-no)\n")
    while again != "Y" and again != "y" and again != "N" and again != "n":
        again = input("Want to try again?(y/Y-yes,n/N-no)\n")
    return (again == "Y" or again == "y")

def main():
    computer_score = 0
    human_score = 0
    instructions()
    computer_score = computer_move(computer_score, human_score)
    human_score = human_move(computer_score, human_score)
    while (computer_score < 100 and human_score < 100) or (computer_score == human_score):
        computer_score = computer_move(computer_score, human_score)
        human_score = human_move(computer_score, human_score)
        if human_score > 100 and human_score > computer_score:
            print("You wins.")
            return
    print("computer wins.")

if __name__ == "__main__":
    main()
