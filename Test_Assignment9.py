"""Module 9 Assignment
Julie Haas
LIS 5937
Spring 2021"""


import unittest


class MyTestCase(unittest.TestCase):

    def test_equal_sets(self):
        x = ['Thirteen', 13, 'Purple', 'tulip']
        y = ['Thirteen', 13, 'Purple', 'pansy']
        self.assertListEqual (x, y, msg = "Lists Are Not Equal")

    def test_almost_equal(self):
        x = 0.092
        y = 0.09
        self.assertAlmostEqual(x, y, msg = "Decimals Not Equal")

    def test_boolean(self):
        x = True
        y = True
        self.assertEqual(x, y, msg = "X and Y are Not Equal")

if __name__ == '__main__':
    unittest.main()
