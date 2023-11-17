#!/usr/bin/python3
"""A simple rock paper scissors game"""
import random


def intro():
    """ INTRO TO THE GAME AND TAKING PLAYER NAME """
    print("🎈Welcome to ULTIMATE ROCK, PAPER, SCISSORS!🎈")
    get_player_name = input("Enter your name: \n>> ").strip()
# Returns player name or a default name(Player 1) if no text is input
    if len(get_player_name) < 1:
        return "Player 1"
    else:
        return get_player_name.upper()


def get_computer_choice():
    """ Randomizing computer selection """
    cases = ["rock", "paper", "scissors"]
    return random.choice(cases)


# PLAYER CHOICE
def get_player_choice():
    """ Takes player input"""
    choice = input("Enter choice: \n>> ").lower()
    # Validating player choice
    choices = ["rock", "paper", "scissors"]
    while choice not in choices:
        print(f"\nPlease choose one of {choices[0]}, {choices[1]} or {choices[2]}")
        choice = input("Enter choice: \n>> ").lower()

    return choice


def main():
    """ Main body of code that computes the player and computer choice and prints out
    the outcome of the game
    """
    player_name = intro()
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        computer_score = 0
        player_score = 0
        if computer_choice == player_choice:
            print(f"Computer is choosing .... \nComputer chooses: {computer_choice} as well")
        else:
            print(f"Computer is choosing .... \nComputer chooses: {computer_choice}")

# OUTCOME
        if player_choice == computer_choice:
            print("\nIt's a TIE!!")
        elif player_choice == "rock" and computer_choice == "scissors":
            print(f"\n{player_name} WINS!!🎉🎉")
            player_score += 1
        elif player_choice == "scissors" and computer_choice == "paper":
            print(f"\n{player_name} WINS!!🎉🎉")
            player_score += 1
        elif player_choice == "paper" and computer_choice == "rock":
            print(f"\n{player_name} WINS!!🎉🎉")
            player_score += 1
        else:
            print("\nYOU LOSE!!🤣🤣😝")
            computer_score += 1

        # Prints out current scores
        print(f"{player_name} : {player_score}   -   Rps AI : {computer_score}")

        # Game Looping
        play_again = input("\nDo you want to play again?(yes or no): \n>> ")
        while play_again not in ("yes", "no"):
            print("\nPlease enter a valid response")
            play_again = input("\nDo you want to play again?(yes or no): \n>> ")

        if play_again.lower().strip() == "no":
            print(f"\nThanks for playing {player_name}, see you soon!✌✌")
            break


if __name__ == "__main__":
    main()
