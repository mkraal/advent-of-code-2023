import re

def main():
    with open('2023-12-04/input.txt') as f:
        raw_input = f.read().split('\n')
    sum = 0
    cards = []
    
    [cards.append({
            "card_num": int(re.search(r'-?\d+', line.split(":")[0]).group()),
            "winning_numbers": re.findall(r'-?\d+', line.split(":")[1].split("|")[0]),
            "my_numbers": re.findall(r'-?\d+',line.split(":")[1].split("|")[1]),
            "win_amount": 0
        }) for line in raw_input]
    
    for card in cards:
        matches = 0
        for number in card["my_numbers"]:
            if number in card["winning_numbers"]:
                if matches == 0: matches = 1
                else: matches *= 2
        sum += matches

    print(sum)   

if __name__ == '__main__':
    main()
