"""
--- Can concat ---
Write a function, can_concat, that takes in a string and a list of words as arguments. The function should return boolean indicating whether or not it is possible to concatenate words of the list together to form the string.

You may reuse words of the list as many times as needed.
"""
import unittest


def can_concat(s, words):
    return _can_concat(s, words, dict())


def _can_concat(s, words, memo):
    if s in memo:
        return memo[s]
    if len(s) == 0:
        return True

    for word in words:
        if not s.startswith(word):
            continue
        new_s = s[len(word):]
        if _can_concat(new_s, words, memo):
            memo[s] = True
            return True

    memo[s] = False
    return False


class Test(unittest.TestCase):
    def test_00(self):
        assert can_concat("oneisnone", ["one", "none", "is"]) == True

    def test_01(self):
        assert can_concat("oneisnone", ["on", "e", "is"]) == False

    def test_02(self):
        assert can_concat("oneisnone", ["on", "e", "is", "n"]) == True

    def test_03(self):
        assert can_concat("foodisgood", ["is", "g", "ood", "f"]) == True

    def test_04(self):
        assert can_concat("santahat", ["santah", "hat"]) == False

    def test_05(self):
        assert can_concat("santahat", ["santah", "san", "hat", "tahat"]) == True

    def test_06(self):
        assert can_concat("rrrrrrrrrrrrrrrrrrrrrrrrrrx", ["r", "rr", "rrr", "rrrr", "rrrrr", "rrrrrr"]) == False


if __name__ == "__main__":
    unittest.main()
