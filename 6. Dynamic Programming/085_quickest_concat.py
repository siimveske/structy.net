"""
--- Quickest concat ---
Write a function, quickest_concat, that takes in a string and a list of words as arguments. The function should return the minimum number of words needed to build the string by concatenating words of the list.

You may use words of the list as many times as needed.
"""
import unittest


def quickest_concat(s, words):
    result = _quickest_concat(s, words, {})
    if result == float('inf'):
        return -1
    else:
        return result


def _quickest_concat(s, words, memo):
    if s in memo:
        return memo[s]
    if s == '':
        return 0

    result = float('inf')
    for word in words:
        if s.startswith(word):
            suffix = s[len(word):]
            r = _quickest_concat(suffix, words, memo) + 1
            result = min(result, r)

    memo[s] = result
    return result


class Test(unittest.TestCase):
    def test_00(self):
        assert quickest_concat('caution', ['ca', 'ion', 'caut', 'ut']) == 2

    def test_01(self):
        assert quickest_concat('caution', ['ion', 'caut', 'caution']) == 1

    def test_02(self):
        assert quickest_concat('respondorreact', ['re', 'or', 'spond', 'act', 'respond']) == 4

    def test_03(self):
        assert quickest_concat('simchacindy', ['sim', 'simcha', 'acindy', 'ch']) == 3

    def test_04(self):
        assert quickest_concat('simchacindy', ['sim', 'simcha', 'acindy']) == -1

    def test_05(self):
        assert quickest_concat('uuuuuu', ['u', 'uu', 'uuu', 'uuuu']) == 2

    def test_06(self):
        assert quickest_concat('rongbetty', ['wrong', 'bet']) == -1

    def test_07(self):
        assert quickest_concat('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu', ['u', 'uu', 'uuu', 'uuuu', 'uuuuu']) == 7


if __name__ == "__main__":
    unittest.main()
