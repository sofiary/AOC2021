#!/usr/bin/python3

####### PART ONE #######
# Count the number of times a depth measurement increases from
# the previous measurement
"""Example:
199 - Start
200 - Increased +1
208 - Increased +1
210 - Increased +1
200 - Decreased
207 - Increased +1
240 - Increased +1
269 - Increased +1
260 - Decreased
263 - Increased +1
"""

####### PART TWO #######



from functools import reduce

def main():
    # Part 1
    with open("2021-1-input.txt","r") as _input:
        _input_text = map(int, _input.read().splitlines())
    _increase_accumulator = 0
    prev_depth = None
    for depth in _input_text:
        if prev_depth is not None and depth > prev_depth:
            _increase_accumulator += 1
        prev_depth = depth
    print(f"Total depth increases: {_increase_accumulator}")

    # Part 2

if __name__ == "__main__":
    main()