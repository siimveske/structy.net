"""
--- Most frequent char ---
Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

You can assume that the input string is non-empty.
"""
import unittest
from collections import defaultdict


def most_frequent_char(string):
    result = ''
    letter_cnt = defaultdict(int)

    for letter in string:
        letter_cnt[letter] += 1

    for letter in string:
        if letter_cnt[letter] > letter_cnt[result]:
            result = letter

    return result


class Test(unittest.TestCase):
    def test_00(self):
        assert most_frequent_char('bookeeper') == 'e'

    def test_01(self):
        assert most_frequent_char('david') == 'd'

    def test_02(self):
        assert most_frequent_char('abby') == 'b'

    def test_03(self):
        assert most_frequent_char('mississippi') == 'i'

    def test_04(self):
        assert most_frequent_char('potato') == 'o'

    def test_05(self):
        assert most_frequent_char('eleventennine') == 'e'

    def test_06(self):
        assert most_frequent_char('riverbed') == 'r'


if __name__ == "__main__":
    unittest.main()
