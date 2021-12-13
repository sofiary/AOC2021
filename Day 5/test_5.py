import numpy as np
import unittest
from part_one_functions import *
from part_two_functions import update_grid as update_grid_part_two

class TestDayFive(unittest.TestCase):

    def setUp(self):
        with open("./Day 5/sample_5_input.txt", "r") as input_:
            data = input_.read().splitlines()
        self.raw_data = data
        self.parsed_data = [
            ((0,9),(5,9)),
            ((8,0),(0,8)),
            ((9,4),(3,4)),
            ((2,2),(2,1)),
            ((7,0),(7,4)),
            ((6,4),(2,0)),
            ((0,9),(2,9)),
            ((3,4),(1,4)),
            ((0,0),(8,8)),
            ((5,5),(8,2)),
        ]
        self.updated_grid = [
            [0,0,0,0,0,0,0,1,0,0],
            [0,0,1,0,0,0,0,1,0,0],
            [0,0,1,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,0,0],
            [0,1,1,2,1,1,1,2,1,1],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [2,2,2,1,1,1,0,0,0,0]
        ]
        self.updated_grid = np.array(self.updated_grid)
        self.updated_grid_part_two = [
            [1,0,1,0,0,0,0,1,1,0],
            [0,1,1,1,0,0,0,2,0,0],
            [0,0,2,0,1,0,1,1,1,0],
            [0,0,0,1,0,2,0,2,0,0],
            [0,1,1,2,3,1,3,2,1,1],
            [0,0,0,1,0,2,0,0,0,0],
            [0,0,1,0,0,0,1,0,0,0],
            [0,1,0,0,0,0,0,1,0,0],
            [1,0,0,0,0,0,0,0,1,0],
            [2,2,2,1,1,1,0,0,0,0],
        ]
        self.updated_grid_part_two = np.array(self.updated_grid_part_two)
        self.dangerous_areas = 5

    def test_parsing_data_to_list(self):
        """Test the data is correctly parsed from the raw format of
        strings in a list into a list of tuples containing tuples, where
        the raw format is 'x1,y1 -> x2,y2'.
        For example, parse '0,9 -> 5,9' into [((0,9),(5,9)), ...]
        """
        parsed_data = parse_data(self.raw_data)
        for tuple_parsed, tuple_test in zip(parsed_data, self.parsed_data):
            self.assertTupleEqual(tuple_parsed, tuple_test)

    def test_grid_setup(self):
        """Test the grid is initialised to be a 2D array of
        x=9 by y=9 length."""
        grid = setup_grid(self.parsed_data)
        self.assertEqual(grid.ndim, 2)
        self.assertEqual(np.sum(grid), 0)
        self.assertEqual(grid.shape, (10,10))

    def test_grid_update_from_data(self):
        """Test that the parsed data upgrades the grid properly.
        """
        grid = np.zeros((10,10), dtype=int)
        updated_grid = update_grid(self.parsed_data, grid)
        np.testing.assert_equal(updated_grid, self.updated_grid)

    def test_diagonal_grid_update_from_data(self):
        """Test that the parsed data updates the grid across the
        linear space and also across the diagonal space.
        """
        grid = np.zeros((10,10), dtype=int)
        updated_grid = update_grid_part_two(self.parsed_data, grid)
        np.testing.assert_equal(updated_grid, self.updated_grid_part_two)

    def test_count_dangerous_areas(self):
        """Test that we can count the number of dangerous areas correctly.
        """
        dangerous_areas = count_dangerous_areas(self.updated_grid)
        self.assertEqual(dangerous_areas, self.dangerous_areas)