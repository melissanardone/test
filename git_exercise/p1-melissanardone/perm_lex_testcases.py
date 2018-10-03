import unittest
import perm_lex

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        """string of two characters"""
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])

    def test_perm_gen_double_letter(self):
        """the same letter is used in a string"""
        self.assertEqual(perm_lex.perm_gen_lex('abb'),['abb','abb', 'bab', 'bba', 'bab', 'bba'])

    def test_perm_gen_lex2(self):
        """string of four characters"""
        self.assertEqual(perm_lex.perm_gen_lex('abcd'),['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba'])

    def test_perm_gen_lex_empty(self):
        """empty string"""
        self.assertEqual(perm_lex.perm_gen_lex(''),[])

    def test_perm_gen_lex_one_char(self):
        """string of one character"""
        self.assertEqual(perm_lex.perm_gen_lex('a'),['a'])

    def test_perm_gen_lex_three_char(self):
        """three character string"""
        self.assertEqual(perm_lex.perm_gen_lex('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

    def test_perm_gen_lex_nine(self):
        """string of 9 character"""
        perm_lex.perm_gen_lex('abcdefghi')

if __name__ == "__main__":
        unittest.main()
