import random
def tie():
  print("Tie !")
def comp_win():    
  print("Computer wins")
def comp_loss():
 print("Computer loss") 
def player_win():
  print("Player has won")
def player_loss():
  print("Player has loss")
        
        
def play_game(player_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chooses {computer_choice}")
    if player_choice==computer_choice:
          tie()
    elif (player_choice== 'rock' and computer_choice=='paper') or \
         (player_choice== 'paper'and computer_choice=='scissors') or \
         (player_choice== 'scissors'and computer_choice=='rock'):
           comp_win()
    else:
      player_win

while True:
   
    player_choice = input("Choose rock, paper, or scissors (or 'q' to quit): ")
    if player_choice == 'q':
        break
    if player_choice not in ['rock', 'paper' , 'scissors']:
      print("Invalid input")
    else: 
      play_game(player_choice)
  
