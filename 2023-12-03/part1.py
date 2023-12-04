import re

def main():
    with open('2023-12-03/input.txt') as f:
        raw_input = f.read()
    special_chars = set(re.findall(r'[^\.\d\n]', raw_input)) # look for all unique special characters
    input = raw_input.split('\n')
    sum = 0
    for i in range(len(input)):
        for match in re.finditer(r'(\d+)', input[i]):
            check_start = 0 if match.start() == 0 else match.start()-1
            check_end = len(input[i]) if match.end() == len(input[i]) else match.end()+1
            compare_current = input[i][check_start: check_end]
            if i == 0:
                # first line only looks current and down
                compare_below = input[i+1][check_start: check_end]
                if any(x in special_chars for x in compare_below) or any(x in special_chars for x in compare_current):
                    print(f"{match.group()}")
                    sum += int(match.group())
            elif i == len(input)-1:
                # last line only looks current and up
                compare_above = input[i-1][check_start: check_end]
                if any(x in special_chars for x in compare_above) or any(x in special_chars for x in compare_current):
                    print(f"{match.group()}")
                    sum += int(match.group())
            else:
                # all other lines look everywhere
                compare_above = input[i-1][check_start: check_end]
                compare_below = input[i+1][check_start: check_end]
                if any(x in special_chars for x in compare_above) or any(x in special_chars for x in compare_below) or any(x in special_chars for x in compare_current):
                    sum += int(match.group())
    print(sum)

if __name__ == '__main__':
    main()