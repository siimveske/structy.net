"""
--- Paired parentheses ---
Write a function, paired_parentheses, that takes in a string as an argument. The function should return a boolean indicating whether or not the string has well-formed parentheses.

You may assume the string contains only alphabetic characters, '(', or ')'.
"""
import unittest


def paired_parentheses(string):
    count = 0
    for character in string:
        if character == '(':
            count += 1
        elif character == ')':
            count -= 1
        if count < 0:
            return False

    return count == 0


class Test(unittest.TestCase):
    def test_00(self):
        assert paired_parentheses("(david)((abby))") == True

    def test_01(self):
        assert paired_parentheses("()rose(jeff") == False

    def test_02(self):
        assert paired_parentheses(")(") == False

    def test_03(self):
        assert paired_parentheses("()") == True

    def test_04(self):
        assert paired_parentheses("(((potato())))") == True

    def test_05(self):
        assert paired_parentheses("(())(water)()") == True

    def test_06(self):
        assert paired_parentheses("(())(water()()") == False

    def test_07(self):
        assert paired_parentheses("") == True

    def test_08(self):
        assert paired_parentheses("))()") == False


if __name__ == "__main__":
    unittest.main()
