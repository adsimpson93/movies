import unittest
from calculations import get_top_genres, get_top_actors, get_top_actors_director_pairs


class moviesTestCase(unittest.TestCase):
    """Test for Calculations.py"""

    def test_top_genres(self):
        testData = [
            ["Action|Comedy|Documentary", "1000", "200"],
            ["Action", "200", "1000"],
            ["Action|Documentary", "400", "100"],
        ]

        self.assertEqual(
            get_top_genres(testData),
            [["Comedy", 800.0], ["Documentary", 550.0], ["Action", 100.0]],
        )

    def test_top_actors(self):
        testData = [
            ["Alex", "Bob", "Charlie", "1000", "200"],
            ["Alex", "", "", "1000", "200"],
            ["", "Bob", "Charlie", "1000", "800"],
            ["Diana", "", "Charlie", "100", "200"],
        ]

        self.assertEqual(
            get_top_actors(testData),
            [["Alex", 800.0], ["Bob", 500.0], ["Charlie", 300.0], ["Diana", -100.0]],
        )

    def test_top_actors_director_pairs(self):
        testData = [
            ["80", "Alex", "Bob", "", "D_Rob"],
            ["100", "Alex", "", "", "D_Tom"],
            ["90", "Bob", "Charlie", "", "D_Rob"],
        ]

        self.assertEqual(
            get_top_actors_director_pairs(testData),
            [
                ["D_Tom", "Alex", 100.0],
                ["D_Rob", "Charlie", 90.0],
                ["D_Rob", "Bob", 85.0],
                ["D_Rob", "Alex", 80.0],
            ],
        )


if __name__ == "__main__":
    unittest.main()

