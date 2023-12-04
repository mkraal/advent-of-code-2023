import re

def main():
    with open('2023-12-04/input-p2.txt') as f:
        raw_input = f.read().split('\n')
    sum = 0
    cards = []
    
    [cards.append({
            "card_num": int(re.search(r'-?\d+', line.split(":")[0]).group()),
            "winning_numbers": re.findall(r'-?\d+', line.split(":")[1].split("|")[0]),
            "my_numbers": re.findall(r'-?\d+',line.split(":")[1].split("|")[1]),
            "num_of_repetitions": 1
        }) for line in raw_input]
    
    for card in cards:
        next_position = 0
        for number in card["my_numbers"]:
            if number in card["winning_numbers"]:
                next_position += 1 
                cards[card["card_num"]+next_position-1]["num_of_repetitions"] += card["num_of_repetitions"]
        sum += card["num_of_repetitions"]
                
    print(sum)

if __name__ == '__main__':
    main()
