import unittest
from bears import *

class TestAssign1(unittest.TestCase):

    def test_bear_01(self):
        """the result should be 42 bears"""
        self.assertTrue(bears(250))

    def test_bear_02(self):
        """starts with 42 bears and should end with 42 bears"""
        self.assertTrue(bears(42))

    def test_bear_03(self):
        """should end up with less than 42 bears"""
        self.assertFalse(bears(53))

    def test_bear_04(self):
        """starts with less than 42 bears"""
        self.assertFalse(bears(41))

    def test_bear_05(self):
        """should end up with 42 bears"""
        self.assertTrue(bears(500))

    def test_bear_06(self):
        """negative number"""
        self.assertFalse(bears(-21))

    def test_bear_07(self):
        """large number"""
        self.assertFalse(bears(10000))

    def test_bear_prime(self):
        """prime number"""
        self.assertFalse(bears(131))

if __name__ == "__main__":
    unittest.main()
