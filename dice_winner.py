
#ask for all player name
#each player roll the dice 10 times
#result form each roll summed up
#player with highest score will will
#when two or more player has same score?
import random
def main():
    winner(3,2)

def winner(player_number,game_round):
    names = []
    score = []
        
    for i in range(player_number):
        name = input("Enter player name: ")
        names.append(name)
        score.append(0)

        
    for i in range(game_round):
        for j in range(player_number):
            input(f"{names[j]},Roll the Dice!")
            result = random.randint(1,6)
            print(f"{result}")
            score[j] = score[j] + result

    with open("score.txt","a") as file:
        file.write(f"{names},{score}")
    print(score)

    winner_index = 0
    winner_score = 0

    for i in range(player_number):
        if score[winner_index] < score[i]:
            winner_score = score[i]
            winner_index = i
        else:
            continue

    return([names[winner_index], winner_score])

if __name__ == "__main__":
    main()

