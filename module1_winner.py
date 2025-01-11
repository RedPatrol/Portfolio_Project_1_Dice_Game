
#ask for all player name
#each player roll the dice certain number of times
#result form each roll summed up
#player with highest score will win
#when two or more player has same score?
#display result on each round?

from display_round_score import display_score
import random


def main():
    winner(3,2)

def winner(player_number,game_round):
    names = []
    score = []
        
    #create lists of players and initiate player score list 
    for i in range(player_number):
        name = input(f"Enter player {i+1} name: ")
        names.append(name)
        score.append(0)

        
    #ask each player to roll and addup their score
    for i in range(game_round):
        for j in range(player_number):
            input(f"{names[j]},Roll the Dice!")
            result = random.randint(1,6)
            print(f"{result}")
            score[j] = score[j] + result

        #create a function to display score in each round
        display_score(i,names,score)
    



    #record score in a text file with timestamped 
    with open("score.txt","a") as file:
        file.write(f"{names},{score}\n")

    #finding winner
    max_index = score.index(max(score))

    return([names[max_index], score[max_index]])

if __name__ == "__main__":
    main()

