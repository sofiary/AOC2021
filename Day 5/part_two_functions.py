from itertools import product
import numpy as np

def parse_data(data: list[str]) -> list[tuple[tuple,tuple]]:
    """Parse a list of raw input strings into the desired output format.
    """
    parsed_data = []
    for line in data:
        split_data = line.split(" -> ")
        split_data = [x.split(",") for x in split_data]
        split_data = [x for y in split_data for x in y]
        split_data = [int(x) for x in split_data]
        parsed_data.append(
                ((split_data[0], split_data[1]),
                (split_data[2], split_data[3]))
                )
    return parsed_data

def setup_grid(data: list[tuple[tuple,tuple]]) -> np.ndarray:
    """Initialise a 2D grid of zeroes of length m x n.
    m is the x-axis length and y is the y-axis length.
    """
    x_max = 0
    y_max = 0
    for tuple_ in data:
        x_max = max([x_max, tuple_[0][0], tuple_[1][0]])
        y_max = max([y_max, tuple_[0][1], tuple_[1][1]])
    return np.zeros((x_max + 1, y_max + 1), dtype=int)

def update_grid(parsed_data: np.ndarray, zeroes_grid: np.ndarray) -> np.ndarray:
    """Update a grid of zeroes with the parsed data to increment each
    grid cell by 1 for every intersecting dangerous area.
    """
    updated_grid = zeroes_grid.copy()
    for tuple_ in parsed_data:
        x1, y1 = tuple_[0][0], tuple_[0][1]
        x2, y2 = tuple_[1][0], tuple_[1][1]
        if x1 == x2:
            for y in np.linspace(y1, y2, 1+abs(y1-y2), dtype=int):
                updated_grid[x1,y] += 1
        elif y1 == y2:
            for x in np.linspace(x1, x2, 1+abs(x1-x2), dtype=int):
                updated_grid[x,y1] += 1
        elif abs(x1 - x2) == abs(y1 - y2):
            for x, y in zip(
                np.linspace(x1, x2, 1+abs(x1-x2), dtype=int),
                np.linspace(y1, y2, 1+abs(y1-y2), dtype=int)
            ):
                updated_grid[x,y] += 1
        else:
            continue
        
    return updated_grid.T

def count_dangerous_areas(
    grid: np.ndarray, dangerous_min: int = 2
    ) -> int:
    """Count the number of dangerous areas in a grid.
    """
    return np.count_nonzero(grid >= dangerous_min)

def part_two(file: str):
    with open(file, "r") as input_:
        data = input_.read().splitlines()
    parsed_data = parse_data(data)
    grid = setup_grid(parsed_data)
    updated_grid = update_grid(parsed_data, grid)
    return count_dangerous_areas(updated_grid)