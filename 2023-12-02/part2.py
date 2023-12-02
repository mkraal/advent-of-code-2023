import re

def extract_numbers_by_color(items, color):
    pattern = rf'(\d+)\s+{color}' 
    numbers = [eval(i) for i in re.findall(pattern, items)]
    return max(numbers)

def multiply_list(input):
    result = 1
    for x in input:
        result = result * x
    return result


def main():
    with open('2023-12-02/input-p2.txt') as f:
        input = f.read().split('\n')
    sum = 0
    for line in input:
        game = line.split(":")
        to_mulitply = []
        for color in ('red', 'blue', 'green'):
            to_mulitply.append(extract_numbers_by_color(game[1], color))
        sum += multiply_list(to_mulitply)
    print(sum)
        
    

if __name__ == "__main__":
    main()