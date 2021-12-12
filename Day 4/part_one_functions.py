from os import read
import numpy as np

def read_bingo_numbers(data: str, delim=",") -> list[int]:
    """Parse a string object into a list of bingo numbers.
    """
    return list(map(int, data.split(delim)))

def create_bingo_boards(data_lines: list) -> dict[int, np.ndarray]:
    """Parse a list object and convert each consecutive line into an ndarray.
    Split boards based on empty lines and number them consecutively.
    """
    boards = {}
    board_num = 0
    board_values = []
    total_lines = len(data_lines)
    for idx, line in enumerate(data_lines, start=1):
        if len(line) != 0:
            board_values.append(list(map(int, line.split())))
        if len(line) == 0 or idx == total_lines:
            boards[board_num] = np.array(board_values)
            board_num += 1
            board_values = []
            continue
    return boards

def check_board_state(bingo_numbers: list, board: np.ndarray) -> bool:
    """Check if the board is a winner.
    It is a winner if the boolean OR of all values across any
    axis is true. Otherwise return false.
    """
    board_bool_array = np.isin(board, bingo_numbers)
    state_x_axis = board_bool_array.all(axis=0)
    state_y_axis = board_bool_array.all(axis=1)
    state = state_x_axis.any() or state_y_axis.any()
    return state

def sum_undrawn_numbers(bingo_numbers: list, board: np.ndarray) -> int:
    board_bool_array = ~np.isin(board, bingo_numbers)
    return np.sum(board, where=board_bool_array)

def part_one(bingo_file: str) -> int:
    with open(bingo_file, "r") as input_:
        data = input_.read().splitlines()
    
    bingo_numbers = read_bingo_numbers(data[0])
    boards = create_bingo_boards(data[2:])
    bingo_rounds = len(bingo_numbers)
    undrawn_sum = None
    for round in range(1, bingo_rounds + 1):
        round_numbers = bingo_numbers[:round]
        # Check boards
        for board in boards.values():
            if check_board_state(round_numbers, board):
                # Winner
                undrawn_sum = sum_undrawn_numbers(round_numbers, board)
                break
        if undrawn_sum: break
        
    return undrawn_sum * bingo_numbers[round-1]