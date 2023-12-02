import re

LIMITS = {'red': 12, 'blue': 14, 'green': 13}

def extract_numbers_by_color(items, color):
    pattern = rf'(\d+)\s+{color}' 
    number = re.findall(pattern, items)
    return int(number[0])

def validate_round(color, round):
    if re.search(color, round):
        return True
    return False


def main():
    with open('2023-12-02/input.txt') as f:
        input = f.read().split('\n')
    sum = 0
    addition = 0
    for line in input:
        game = line.split(":")
        rounds = game[1].split(";")
        addition = ''.join(re.findall(r'-?\d+', game[0]))
        for round in rounds:
            for color in LIMITS:
                if validate_round(color, round):
                    if extract_numbers_by_color(round, color) > LIMITS[color]:
                        addition = 0
        sum += int(addition)
        print(sum)
        
    

if __name__ == "__main__":
    main()