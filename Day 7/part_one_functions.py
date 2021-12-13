def part_one(file: str) -> int:
    with open(file, "r") as input_:
        crab_positions = list(map(int,input_.read().split(",")))
    
    position_cost = []
    position_range = range(
        min(crab_positions),
        max(crab_positions) + 1,
    )

    for position in position_range:
        position_cost.append(
            (position, sum(list(map(lambda x: abs(x-position), crab_positions))))
        )

    return sorted(position_cost, key=lambda x: x[1], reverse=False).pop(0)[1]