def part_one(file: str, days: int = 80):
    with open(file, "r") as input_: 
        lanternfish = list(map(int,input_.read().split(",")))
    
    for day in range(0, days+1):
        print(f"Fish on day {day}: {len(lanternfish)}.")
        lanternfish = [x-1 for x in lanternfish]
        new_fish = len([x for x in lanternfish if x == -1])
        lanternfish = list(map(lambda x: x if x != -1 else 6, lanternfish))
        lanternfish.extend([8] * new_fish)