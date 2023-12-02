import re

with open('2023-12-01/input-p2.txt') as f:
    input = f.read().split('\n')


NUMBER_MAP_2 = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def get_indexed_numbers(string:str) -> dict:
    """Get a map of occurences of both numberical and text numbers"""
    all_nums = {}
    for i in NUMBER_MAP_2:
        indexes = [m.start() for m in re.finditer(i, string)] + [m.start() for m in re.finditer(str(NUMBER_MAP_2[i]), string)]
        indexes.sort()
        all_nums.update({NUMBER_MAP_2[i]: indexes})
    return all_nums

def get_two_digit_number(number_map:dict) -> int:
    """Get the numbers with smallest and largest index and return them as a two digit number"""
    min_val, max_val = float('inf'), float('-inf')
    min_key, max_key = 0, 0

    for key, values in number_map.items():
        if values: 
            current_min, current_max = min(values), max(values)
            if current_min < min_val:
                min_val, min_key = current_min, key
            if current_max > max_val:
                max_val, max_key = current_max, key

    return (min_key * 10) + max_key
    


def main():
    with open('2023-12-01/input-p2.txt') as f:
        input = f.read().split('\n')
    sum = 0
    for line in input:
        num_map = get_indexed_numbers(line)
        sum += get_two_digit_number(num_map)
    print(sum)

if __name__ == "__main__":
    main()


