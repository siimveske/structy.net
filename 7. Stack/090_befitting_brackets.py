"""
--- Befitting brackets ---
Write a function, befitting_brackets, that takes in a string as an argument. The function should return a boolean indicating whether or not the string contains correctly matched brackets.

You may assume the string contains only characters: ( ) [ ] { }
"""


import unittest


def befitting_brackets(string):
    stack = []
    brace_map = {
        "(": ")", "[": "]", "{": "}"
    }

    for character in string:
        if character in ["(", "[", "{"]:
            stack.append(character)
        else:
            if not stack:
                return False
            last_item = stack.pop()
            if brace_map[last_item] != character:
                return False

    return stack == []


class Test(unittest.TestCase):
    def test_00(self):
        assert befitting_brackets('(){}[](())') == True

    def test_01(self):
        assert befitting_brackets('({[]})') == True

    def test_02(self):
        assert befitting_brackets('[][}') == False

    def test_03(self):
        assert befitting_brackets('{[]}({}') == False

    def test_04(self):
        assert befitting_brackets('[]{}(}[]') == False

    def test_05(self):
        assert befitting_brackets('[]{}()[]') == True

    def test_06(self):
        assert befitting_brackets(']{}') == False

    def test_07(self):
        assert befitting_brackets('') == True

    def test_08(self):
        assert befitting_brackets("{[(}])") == False


if __name__ == "__main__":
    unittest.main()
