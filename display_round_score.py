def main():
    display_score(1,["a","b","c"],[2,4,6])

def display_score(round,name_list,score_list):
    print(f"Round {round + 1} score:")
    for i in range(len(name_list)):
        print(f"{name_list[i]}:{score_list[i]}")


if __name__ == "__main__":
    main()