"""
Automated Tests for Bandwidth Allocation
"""

import unittest

from allocator import allocate, fixed_equal


class TestBandwidthAllocation(unittest.TestCase):

    def test_equal_weight_example(self):

        result = allocate(
            100,
            [10, 30, 80],
            [1, 1, 1]
        )

        expected = [10, 30, 60]

        for actual, target in zip(result, expected):
            self.assertAlmostEqual(actual, target)


    def test_weighted_example(self):

        result = allocate(
            100,
            [10, 40, 80],
            [5, 3, 2]
        )

        expected = [10, 40, 50]

        for actual, target in zip(result, expected):
            self.assertAlmostEqual(actual, target)


    def test_underloaded_network(self):

        result = allocate(
            100,
            [10, 20, 30],
            [1, 1, 1]
        )

        self.assertAlmostEqual(
            sum(result),
            60
        )


    def test_capacity_constraint(self):

        result = allocate(
            100,
            [50, 60, 80],
            [1, 1, 1]
        )

        self.assertLessEqual(
            sum(result),
            100 + 1e-9
        )


    def test_demand_constraint(self):

        demands = [10, 30, 80]

        result = allocate(
            100,
            demands,
            [1, 1, 1]
        )

        for allocation, demand in zip(result, demands):

            self.assertLessEqual(
                allocation,
                demand + 1e-9
            )


    def test_invalid_weights(self):

        with self.assertRaises(ValueError):

            allocate(
                100,
                [10, 20],
                [1, 0]
            )


    def test_fixed_equal(self):

        result = fixed_equal(
            100,
            [10, 30, 80]
        )

        self.assertAlmostEqual(
            sum(result),
            73.33333333333333
        )


if __name__ == "__main__":
    unittest.main()
