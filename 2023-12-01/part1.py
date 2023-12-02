import re

with open('2023-12-01/input.txt') as f:
    input = f.read().split('\n')


def get_two_digit_number(calibration_value: str) -> int:
    """Gets all numbers from a string"""
    all_nums = re.sub('\\D', "", calibration_value)
    return int(all_nums[0] + all_nums[-1])

def running_sum_generator():
    total = 0
    while True:
        new_number = yield total
        if new_number is not None:
            total += new_number
def main():    
    sum_gen = running_sum_generator()
    next(sum_gen)
    for calibration_value in input:
        num = get_two_digit_number(calibration_value)
        running_total = sum_gen.send(num)

    print(running_total)

if __name__ == "__main__":
    main()

