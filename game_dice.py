#multiplayer game
#ask how many player are playing?
from dice_winner import winner

while True:
    try:
        number_of_player = int(input("How many player would like to play this game?"))
        break
    except ValueError:
        print("Error! Enter valid input")
        continue

while True:
    try:
        game_round = int(input("How many rounds would you like to play?"))
        break
    except ValueError:
        print("Error! Enter valid input")
        continue

winner(number_of_player,game_round)

#ask name?
#roll a dice for each and keep adding the score for 10 rounds?
#player with highest sum will win

