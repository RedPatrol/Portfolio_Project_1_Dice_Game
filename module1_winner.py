#each player roll the dice certain number of times
#result form each roll summed up
#player with highest score will win
#when two or more player has same score rematch

from display_round_score import display_score
import random


def main():
    test_players = ["sujan","ushma"]
    winner_name, winner_score = winner(test_players,2)
    print(f"winner is {winner_name}. Score : {winner_score}.")

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

    #check if there is tie
    max_score = max(score)

    #count number of player with max score
    tie_player_number = score.count(max(score))
    tie_players = [] * tie_player_number

    if tie_player_number > 1:
        print("Wow! There is a tie.\n Get ready for a rematch.")
        for i in range(len(score)):
            if score[i] == max_score:
                tie_players.append(player_names[i])
        return winner(tie_players,2)
    else:
        #finding winner
        max_index = score.index(max_score)
        return([player_names[max_index], score[max_index]])

if __name__ == "__main__":
    main()

