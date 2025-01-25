
#ask for all player name
#each player roll the dice certain number of times
#result form each roll summed up
#player with highest score will win
#when two or more player has same score?
#display result on each round?

from display_round_score import display_score
from tie_breaker import tie_breaker
import random


def main():
    winner(3,2)

def winner(player_names,game_round):
    player_number = len(player_names)
    score = [0] * len(player_names)
        
    #ask each player to roll and addup their score
    for i in range(game_round):
        for j in range(player_number):
            input(f"{player_names[j]},Roll the Dice!")
            result = random.randint(1,6)
            print(f"{result}")
            score[j] = score[j] + result

        #create a function to display score in each round
        display_score(i,player_names,score)
    



    #record score in a text file with timestamped 
    with open("score.txt","a") as file:
        file.write(f"{player_names},{score}\n")

    """#check if there is tie
    #count number of player with max score
    tie_players_number = score.count(max(score))

    if tie_players_number > 1:
        print("Wow! There is a tie.\n Get ready for a rematch.")
        
        # following function is yet to create
        tie_breaker(player_names,score)"""

    #finding winner
    max_index = score.index(max(score))

    return([player_names[max_index], score[max_index]])

if __name__ == "__main__":
    main()

