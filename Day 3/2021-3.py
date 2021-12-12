#!/usr/bin/python3

""" PART ONE
Upon receiving multiple lines of bits, calculate the gamma rate and 
the epsilon rate.

The gamma rate is calculated based on the following:
1. Get the most common bit in each bit column
2. Translate the most common bits into a binary integer

The epsilon rate is calculated based on the inverse of the gamma rate.

The power consumption is the final value to calculate.
It can be calculated as the multiple  of the gamma rate and the epsilon rate.
"""

""" PART TWO
Verify the life support rating. The life support rating is equal to the
oxygen generator rating multipled by the CO2 scrubber rating.

For the oxygen generator rating:
1. Filter rows of bits by each column iteratively
2. Keep only the rows which have the most common bit in that bit's position
3. If 1 and 0 are equal in number of occurences, filter zeroes

For the CO2 scrubber rating, do the opposite of the oxygen generator rating.

The life support rating can now be calculated.
"""

from collections import defaultdict
from part_two_functions import * # Don't try this at home :)

def part_one():
    with open("./Day 3/2021-3_input.txt", "r") as input_:
        input_text = input_.read().splitlines()
    total_lines = len(input_text)
    bit_position_dict = defaultdict(lambda: 0)

    for binary_string in input_text:
        for idx, bit in enumerate(binary_string):
            bit_position_dict[idx] += int(bit)

    gamma = ""
    epsilon = ""

    for key, val in bit_position_dict.items():
        print(key)
        gamma += "1" if val > total_lines / 2 else "0"
        epsilon += "0" if val > total_lines / 2 else "1"

    gamma_int = int(gamma, 2)
    epsilon_int = int(epsilon, 2)
    power_consumption = gamma_int * epsilon_int

    print(
        f"Gamma: {gamma_int}, Epsilon: {epsilon_int}, "
        f"Power Consumption: {power_consumption}."
        )

def part_two():
    with open("./Day 3/2021-3_input.txt", "r") as input_:
        input_text = input_.read().splitlines()

    ratings = get_ratings(input_text)
    for key, val in ratings.items():
        print(f"{key}: {val}")

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()