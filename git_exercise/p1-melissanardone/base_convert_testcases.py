import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        """convert number to binary"""
        self.assertEqual(convert(45,2),"101101")

    def test_base4(self):
        """convert number to base 4"""
        self.assertEqual(convert(30,4),"132")

    def test_base5(self):
        """convert number to base 5"""
        self.assertEqual(convert(671,5), "10141")

    def test_base16(self):
        """convert number to hex"""
        self.assertEqual(convert(316,16),"13C")
        self.assertEqual(convert(175,16),"AF")

if __name__ == "__main__":
        unittest.main()