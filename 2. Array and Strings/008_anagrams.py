"""
--- Anagrams ---
Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.
"""

import unittest
from collections import defaultdict


def anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    s1_letter_count = defaultdict(int)
    s2_letter_count = defaultdict(int)

    for idx in range(len(s1)):
        s1_letter_count[s1[idx]] += 1
        s2_letter_count[s2[idx]] += 1

    return s1_letter_count == s2_letter_count


class Test(unittest.TestCase):
    def test_00(self):
        assert anagrams('restful', 'fluster') == True

    def test_01(self):
        assert anagrams('cats', 'tocs') == False

    def test_02(self):
        assert anagrams('monkeyswrite', 'newyorktimes') == True

    def test_03(self):
        assert anagrams('paper', 'reapa') == False

    def test_04(self):
        assert anagrams('elbow', 'below') == True

    def test_05(self):
        assert anagrams('tax', 'taxi') == False

    def test_06(self):
        assert anagrams('taxi', 'tax') == False

    def test_07(self):
        assert anagrams('night', 'thing') == True

    def test_08(self):
        assert anagrams('abbc', 'aabc') == False


if __name__ == "__main__":
    unittest.main()
