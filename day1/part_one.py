from typing.io import TextIO


def get_max_calories(file: TextIO):
    calories_sum, max_calories = 0, 0
    for line in file.readlines():
        if line.strip("\n").isalnum():
            calories_sum += int(line)
        else:
            max_calories = max(max_calories, calories_sum)
            calories_sum = 0
    return max_calories


if __name__ == "__main__":
    f = open("input.txt", "r")
    calories = get_max_calories(f)
    f.close()
    print("Most calories: ", calories)
