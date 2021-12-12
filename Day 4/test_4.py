import numpy as np
import unittest
from part_one_functions import *

class TestDayFour(unittest.TestCase):

    def setUp(self):
        with open("./Day 4/sample_4_input.txt", "r") as data:
            self.data = data.read().splitlines()
        self.winning_numbers = [1,2,3,4,5,6]

    def test_read_bingo_numbers(self):
        """Verify parsed bingo numbers are in a list
        """
        data = "1,2,3"
        self.assertListEqual(
            read_bingo_numbers(data),
            [1,2,3]
        )

    def test_create_bingo_boards(self):
        boards = create_bingo_boards(self.data[2:])


    def test_check_bingo_board_state(self):
        """Return true if the bingo board is a winner.
        Return false if the bingo board is not a winner.
        """
        winner_board = np.array(
            [
                [ 1,  2, 5],
                [11, 66, 4],
                [90,  5, 6]
            ]
        )
        loser_board = np.array(
            [
                [11, 77, 22],
                [ 3, 88, 21],
                [ 9,  7, 28]
            ]
        )

        self.assertTrue(check_board_state(self.winning_numbers, winner_board))
        self.assertFalse(check_board_state(self.winning_numbers, loser_board))

    def test_sum_undrawn_numbers(self):
        """Calculate the sum of numbers which have not been
        drawn in the bingo round, on the winning board.
        """
        winner_board = np.array(
            [
                [ 1, 2, 3],
                [ 9, 8, 4],
                [ 6, 5, 7]
            ]
        )
        
        self.assertEqual(
            sum_undrawn_numbers(self.winning_numbers, winner_board),
            24
            )

    