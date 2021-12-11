#!/usr/bin/python3

""" PART ONE
The submarine can take a series of commands:
- 1. Forward x units
- 2. Depth increase by x units
- 3. Depth decrease by x units

The submarine receives a planned course as input.
Example:
forward 5
down 5
forward 8
up 3
down 8...

Horizontal and depth positions start at 0
Get the sum of each directional axes' movement based on inputs
Multiply the two sums together
"""

""" PART TWO
The submarine now has another tracked axes - aim.
Aim also starts at 0.
Aim is a function of movement across the other two axes.
Moving down increases aim by x, moving up decreases aim by x.
Moving forward increases depth by the multiple of aim and x.
"""

def part_one():
    with open("./Day 2/2021-2_input.txt", "r") as input_:
        input_text = input_.read().splitlines()
    loc_x = 0
    loc_y = 0

    for movement in input_text:
        direction, distance = movement.split(" ")
        distance = int(distance)
        match direction:
            case "forward":
                loc_x += distance
            case "up":
                loc_y += distance
            case "down":
                loc_y -= distance
            case _:
                raise ValueError("Unknown direction.")

    print(
        f"Multiple of axis x = {loc_x} and axis y = {loc_y} "
        f"is equal to {loc_x * loc_y}."
        )

def part_two():
    with open("./Day 2/2021-2_input.txt", "r") as input_:
        input_text = input_.read().splitlines()
    loc_x = 0
    loc_y = 0
    loc_aim = 0

    for movement in input_text:
        direction, distance = movement.split(" ")
        distance = int(distance)
        match direction:
            case "forward":
                loc_x += distance
                loc_y += (loc_aim * distance)
            case "up":
                loc_aim += distance
            case "down":
                loc_aim -= distance
            case _:
                raise ValueError("Unknown direction.")

    print(
        f"Multiple of axis x = {loc_x} and axis y = {loc_y} "
        f"is equal to {loc_x * loc_y}."
        )

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()