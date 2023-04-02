import random

def play_game(player_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chooses {computer_choice}")

    if player_choice == computer_choice:
        print("Tie game!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        print("Player wins!")
    else:
        print("Computer wins!")

# Main loop
while True:
    # Get player choice
    player_choice = input("Choose rock, paper, or scissors (or 'q' to quit): ")
    if player_choice == 'q':
        break

    # Play game
    if player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose again.")
    else:
        play_game(player_choice)
