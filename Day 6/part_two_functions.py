from collections import Counter

def part_two(file: str, days: int = 256):
    with open(file, "r") as input_: 
        lanternfish = Counter(list(map(int,input_.read().split(","))))
    
    for day in range(0, days+1):
        print(f"Fish on day {day}: {lanternfish.total()}.")
        new_fish = lanternfish[0]
        for idx in range(0,8):
            lanternfish[idx] = lanternfish[idx+1] if idx != 6 else \
                lanternfish[idx+1] + new_fish
        lanternfish[8] = new_fish
        