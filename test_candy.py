import unittest

from candy import average_candy, best_house, report, total_candy


class CandyTrackerTests(unittest.TestCase):
    def setUp(self):
        self.houses = [
            {"name": "Pumpkin Manor", "candy": 10},
            {"name": "Ghost House", "candy": 0},
            {"name": "Witch's Hollow", "candy": 20},
        ]

    def test_total_candy(self):
        self.assertEqual(total_candy(self.houses), 30)

    def test_average_candy(self):
        self.assertAlmostEqual(average_candy(self.houses), 10)

    def test_best_house(self):
        self.assertEqual(best_house(self.houses), {"name": "Witch's Hollow", "candy": 20})

    def test_zero_candy_warning(self):
        self.assertIn("This house is haunted!", report(self.houses))

    def test_empty_list_does_not_crash(self):
        self.assertEqual(total_candy([]), 0)
        self.assertEqual(average_candy([]), 0)
        self.assertIsNone(best_house([]))
        self.assertIn("No houses visited", report([]))


if __name__ == "__main__":
    unittest.main()
