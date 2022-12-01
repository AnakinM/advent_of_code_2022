from typing.io import TextIO


def get_top_max_calories_sum(file: TextIO):
    calories_sum = 0
    top_calories = []
    for line in file.readlines():
        if line.strip("\n").isalnum():
            calories_sum += int(line)
        else:
            if len(top_calories) < 3:
                top_calories.append(calories_sum)
            elif calories_sum > min(top_calories):
                top_calories.remove(min(top_calories))
                top_calories.append(calories_sum)
            calories_sum = 0
    return sum(top_calories)


if __name__ == "__main__":
    f = open("input.txt", "r")
    calories = get_top_max_calories_sum(f)
    f.close()
    print("Most calories: ", calories)
