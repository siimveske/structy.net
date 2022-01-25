import unittest

"""
--- Max palin subsequence ---
Write a function, max_palin_subsequence, that takes in a string as an argument. The function should return the length of the longest subsequence of the string that is also a palindrome.

A subsequence of a string can be created by deleting any characters of the string, while maintaining the relative order of characters.
"""


def max_palin_subsequence(string):
    return calculate(string, (0, len(string) - 1), {})


def calculate(string, idx, memo):
    start, end = idx
    if idx in memo:
        return memo[idx]
    if start > end:
        return 0
    if start == end:
        return 1

    result = 0
    if string[start] == string[end]:
        result += 2 + calculate(string, (start + 1, end - 1), memo)
    else:
        right = calculate(string, (start + 1, end), memo)
        left = calculate(string, (start, end - 1), memo)
        result += max(right, left)

    memo[idx] = result
    return memo[idx]


class Test(unittest.TestCase):

    def test_00(self):
        assert max_palin_subsequence("luwxult") == 5

    def test_01(self):
        assert max_palin_subsequence("xyzaxxzy") == 6

    def test_02(self):
        assert max_palin_subsequence("lol") == 3

    def test_03(self):
        assert max_palin_subsequence("boabcdefop") == 3

    def test_04(self):
        assert max_palin_subsequence("z") == 1

    def test_05(self):
        assert max_palin_subsequence("chartreusepugvicefree") == 7

    def test_06(self):
        assert max_palin_subsequence("qwueoiuahsdjnweuueueunasdnmnqweuzqwerty") == 15

    def test_07(self):
        assert max_palin_subsequence("enamelpinportlandtildecoldpressedironyflannelsemioticsedisonbulbfashionaxe") == 31


if __name__ == "__main__":
    unittest.main()
