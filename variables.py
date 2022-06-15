import random
import os
import shutil

path = "C:\\Users\\tijnf\\Documents\\kopie van map\\rps_score.txt"


with open(path, "r") as file:
    lines = file.readlines()
    print(lines[15:17])
    score = {"player": 0,
             "computer": 0}


def player_win():
    print("Player wins!")
    updated_key = "player"
    score[updated_key] += 1


def computer_win():
    print("Computer wins!")
    updated_key = "computer"
    score[updated_key] += 1


while True:
    options = ["Rock", "Paper", "Scissors", "gun"]
    computer_choice = random.choice(options[:3])

    player_choice = ""
    while player_choice not in options:
        player_choice = input("Rock, Paper or Scissors?: ").capitalize()


    def choices():
        print(f"player: {player_choice}\n"
              f"computer: {computer_choice}")


    if player_choice == computer_choice:
        choices()
        print("tie!")

    elif player_choice == "Rock":
        if computer_choice == "Scissors":
            choices()
            player_win()
        if computer_choice == "Paper":
            choices()
            computer_win()

    elif player_choice == "Paper":
        if computer_choice == "Scissors":
            choices()
            computer_win()
        if computer_choice == "Paper":
            choices()
            player_win()

    elif player_choice == "Scissors":
        if computer_choice == "Rock":
            choices()
            computer_win()
        if computer_choice == "Paper":
            choices()
            player_win()

    print(score)
    play_again = input("do you want to play again? (yes/no): ")

    if play_again != "yes":
        break

with open(path, 'w') as File:
    File.write(f'player score is {str(score["player"])}\n'
               f'computer score is {str(score["computer"])}')
print("Score saved.")
