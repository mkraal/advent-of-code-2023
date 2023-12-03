import re


def get_coordinates(input):
    "Returns all occurences of star signs and numbers with their coordinates"
    stars = []
    numbers = []
    for i in range(len(input)):
        for match in re.finditer(r"(\d+)", input[i]):
            numbers.append(
                {
                    "row": i,
                    "value": match.group(),
                    "start": match.start(),
                    "end": match.end(),
                }
            )
        for j in range(len(input[i])):
             if input[i][j] == "*":
                stars.append([i, j])
    return (stars, numbers)


def is_below(star, number):
    "Checks whether a number is below or diagonally down from a star"
    left = number["start"] - 1
    right = number["end"]
    if (star[0] + 1 == number["row"]) and (left <= star[1] <= right):
        return True
    return False


def is_above(star, number):
    "Checks whether a number is above or diagonally up from a star"
    left = number["start"] - 1
    right = number["end"]
    if star[0] - 1 == number["row"] and (left <= star[1] <= right):
        return True
    return False


def is_row_neighbour(star, number):
    "Checks whether a number is right next to a start (possible from both sides)"
    if star[0] == number["row"] and (
        star[1] == number["end"] or star[1] == number["start"]-1
    ):
        return True
    return False


def main():
    with open("2023-12-03/input-p2.txt") as f:
        input = f.read().split("\n")

    sum = 0
    star_value_combinations = []
    coordinates = get_coordinates(input)
    stars, numbers = coordinates[0], coordinates[1]
    for star in stars:
        # Iterate over map of stars
        one_star_numbers = []
        for number in numbers:
            # Iterate over numbers and try to check whether they satisfy the conditions
            if (
                is_below(star, number)
                or is_above(star, number)
                or is_row_neighbour(star, number)
            ):
                # if they do, append them to a list of possible numbers
                one_star_numbers.append(number)
        # at the end, append the star - number neighbor combinations to a list
        star_value_combinations.append({"star": star, "numbers": one_star_numbers})
    print(star_value_combinations)
    for star in star_value_combinations:
        if len(star["numbers"]) == 2:
            # If a star has exactly 2 neighbors, multiply them and add them to the sum
            sum += int(star["numbers"][0]["value"]) * int(star["numbers"][1]["value"])
    print(sum)


if __name__ == "__main__":
    main()