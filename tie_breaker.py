
from module1_winner import winner

def main():
    test_players = ["sujan","ushma","dev","maya"]
    test_scores = [5,5,5,2]

    tie_breaker(test_players,test_scores)
    

def tie_breaker(player_names,scores):
    tie_players_index = []
    tie_players_list = []

    player_number = len(scores)

    max_score = max(scores)

    tie_player = scores.count(max_score)

    if tie_player > 1:
        for i in range(player_number):
            if scores[i] == max_score:
                tie_players_index.append(i)
            else:
                continue

    for i in range(len(tie_players_index)):
        tie_players_list.append(player_names[tie_players_index[i]])
    
    
    winner(tie_players_list,2)

    

if __name__ == "__main__":
    main()












