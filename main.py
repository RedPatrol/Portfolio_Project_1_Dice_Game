#ask for inputs: number of players, game round
#calls another function with these input for rest of the game

from module1_winner import winner

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

