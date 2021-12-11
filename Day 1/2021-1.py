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
# Count the number of times a depth measurement across a
# sliding window of values (n) increases, where n=3

def part_one():
    with open("./Day 1/2021-1_pt1_input.txt","r") as input_:
        input_text = map(int, input_.read().splitlines())
    increase_accumulator = 0
    prev_depth = None
    for depth in input_text:
        if prev_depth is not None and depth > prev_depth:
            increase_accumulator += 1
        prev_depth = depth
    print(f"Total depth increases: {increase_accumulator}")
    
def part_two():
    with open("./Day 1/2021-1_pt1_input.txt","r") as input_:
        input_text = list(map(int, input_.read().splitlines()))
    increase_accumulator = 0
    prev_depth = None
    n = 3
    for idx, _ in enumerate(input_text, start=n):
        depth = sum(input_text[idx-n:idx])
        if prev_depth is not None and depth > prev_depth:
            increase_accumulator += 1
        prev_depth = depth
    print(f"Total sliding window depth increases: {increase_accumulator}")

def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()