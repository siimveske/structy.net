"""
--- Most frequent char ---
Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

You can assume that the input string is non-empty.
"""
import unittest
from collections import defaultdict


def most_frequent_char(string):
    max_cnt = 0
    letter_cnt = defaultdict(int)
    cnt_to_letter = defaultdict(list)

    for letter in string:
        letter_cnt[letter] += 1
        cnt_to_letter[letter_cnt[letter]].append(letter)
        if letter_cnt[letter] > max_cnt:
            max_cnt = letter_cnt[letter]

    first_letter_idx = len(string)
    for letter in cnt_to_letter[max_cnt]:
        letter_idx = string.index(letter)
        if letter_idx < first_letter_idx:
            first_letter_idx = letter_idx

    return string[first_letter_idx]


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
