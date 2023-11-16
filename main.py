import random


# INTRO TO THE GAME AND TAKING PLAYER NAME
def intro():
    print("🎈Welcome to ULTIMATE ROCK, PAPER, SCISSORS!🎈")
    get_player_name = input("Enter your name: \n>> ").strip()
# Returns player name or a default name(Player 1) if no text is input
    if len(get_player_name) < 1:
        return "Player 1"
    else:
        return get_player_name.upper()


# Randomizing computer selection
def get_computer_choice():
    cases = ["rock", "paper", "scissors"]
    return random.choice(cases)


# PLAYER CHOICE
# Takes in player choice
def get_player_choice():
    choice = input("Enter choice: \n>> ")
    return choice.lower()


# Main body of code that computes the player and computer choice and prints out
# the outcome of the game
def main():
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

        print(f"{player_name} : {player_score}   -   Rps AI : {computer_score}")
        play_again = input("\nDo you want to play again?(yes or no): \n>> ")
        if play_again.lower().strip() == "no":
            print(f"\nThanks for playing {player_name}, see you soon!✌✌")
            break


if __name__ == "__main__":
    main()
