def get_choice(opponent_choice: str, result: str) -> str:
    if opponent_choice == "A" and result == "Z":
        return "B"
    elif opponent_choice == "A" and result == "Y":
        return "A"
    elif opponent_choice == "A" and result == "X":
        return "C"
    elif opponent_choice == "B" and result == "X":
        return "A"
    elif opponent_choice == "B" and result == "Y":
        return "B"
    elif opponent_choice == "B" and result == "Z":
        return "C"
    elif opponent_choice == "C" and result == "X":
        return "B"
    elif opponent_choice == "C" and result == "Y":
        return "C"
    elif opponent_choice == "C" and result == "Z":
        return "A"


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
        if me == "X":
            my_score += points[get_choice(opponent, me)]
            opponent_score += WIN + points[opponent]
        elif me == "Y":
            my_score += DRAW + points[get_choice(opponent, me)]
            opponent_score += DRAW + points[opponent]
        elif me == "Z":
            my_score += WIN + points[get_choice(opponent, me)]
            opponent_score += points[opponent]
    print("My score: ", my_score)
    print("Opponent score: ", opponent_score)
