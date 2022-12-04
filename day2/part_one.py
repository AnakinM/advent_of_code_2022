def result(opponent_choice: str, my_choice: str) -> str:
    if opponent_choice == "A" and my_choice == "Z":
        return opponent_choice
    elif opponent_choice == "A" and my_choice == "Y":
        return my_choice
    elif opponent_choice == "B" and my_choice == "X":
        return opponent_choice
    elif opponent_choice == "B" and my_choice == "Z":
        return my_choice
    elif opponent_choice == "C" and my_choice == "Y":
        return opponent_choice
    elif opponent_choice == "C" and my_choice == "X":
        return my_choice
    elif (opponent_choice == "A" and my_choice == "X") \
            or (opponent_choice == "B" and my_choice == "Y") \
            or (opponent_choice == "C" and my_choice == "Z"):
        return "DRAW"


if __name__ == "__main__":
    points = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    DRAW = 3
    WIN = 6
    my_score = 0
    opponent_score = 0
    guide = open("input.txt", "r").readlines()
    for line in guide:
        opponent, me = tuple(line.strip("\n").split(" "))
        if result(opponent, me) == "DRAW":
            my_score += DRAW + points[me]
            opponent_score += DRAW + points[opponent]
        elif result(opponent, me) == me:
            my_score += WIN + points[me]
            opponent_score += points[opponent]
        elif result(opponent, me) == opponent:
            my_score += points[me]
            opponent_score += WIN + points[opponent]
    print("My score: ", my_score)
    print("Opponent score: ", opponent_score)
