"""
--- Nesting score ---
Write a function, nesting_score, that takes in a string of brackets as an argument. The function should return the score of the string according to the following rules:
    1. [] is worth 1 point
    2. XY is worth m + n points where X, Y are substrings of well-formed brackets and m, n are their respective scores
    3. [S] is worth 2 * k points where S is a substring of well-formed brackets and k is the score of that substring

You may assume that the input only contains well-formed square brackets.
"""
import unittest


def nesting_score(string):
    stack = [0]
    for character in string:
        if character == "[":
            stack.append(0)
        else:
            top = stack.pop()
            if top == 0:
                stack[-1] += 1
            else:
                stack[-1] += top * 2
    return stack.pop()


class Test(unittest.TestCase):
    def test_00(self):
        assert nesting_score("[]") == 1

    def test_01(self):
        assert nesting_score("[][][]") == 3

    def test_02(self):
        assert nesting_score("[[]]") == 2

    def test_03(self):
        assert nesting_score("[[][]]") == 4

    def test_04(self):
        assert nesting_score("[[][][]]") == 6

    def test_05(self):
        assert nesting_score("[[][]][]") == 5

    def test_06(self):
        assert nesting_score("[][[][]][[]]") == 7

    def test_07(self):
        assert nesting_score("[[[[[[[][]]]]]]][]") == 129


if __name__ == "__main__":
    unittest.main()
