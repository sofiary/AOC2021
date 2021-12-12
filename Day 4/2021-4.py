#!/usr/bin/python3

from part_one_functions import part_one
from part_two_functions import part_two

def main():
    file = "./Day 4/2021-4_input.txt"
    print(part_one(bingo_file=file))
    print(part_two(bingo_file=file))

if __name__ == "__main__":
    main()
