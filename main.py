#ask for inputs: number of players, game round
#calls another function with these input for rest of the game

#module1_winner is file name, winner is function in that file
from module1_winner import winner
player_names = []

#validate input - player number
while True:
    try:
        number_of_player = int(input("How many player would like to play this game?"))
        if number_of_player >= 2:
            break
        else:
            print("At least two player required!")
            
    except ValueError:
        print("Error! Enter valid input")
        continue

#validate input - game_round
while True:
    try:
        game_round = int(input("How many rounds would you like to play?"))
        break
    except ValueError:
        print("Error! Enter valid input")
        continue
      
#create lists of players
for i in range(number_of_player):
    name = input(f"Enter player {i+1} name: ")
    player_names.append(name)
     
#call function
winner,score = winner(player_names,game_round)
print(f"{winner.upper()} is the winner with score {score}.")

