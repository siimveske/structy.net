"""
--- Decompress braces ---
Write a function, decompress_braces, that takes in a compressed string as an argument. The function should return the string decompressed.

The compression format of the input string is 'n{sub_string}', where the sub_string within braces should be repeated n times.

You may assume that every number n is guaranteed to be an integer between 1 through 9.

You may assume that the input is valid and the decompressed string will only contain alphabetic characters.
"""
import unittest


def decompress_braces(string):
    stack = []
    for character in string:
        if character.isalnum():
            stack.append(character)
        elif character == '}':
            pattern = ''
            item = stack.pop()
            while item.isalpha():
                pattern = item + pattern
                item = stack.pop()
            qty = int(item)
            stack.append(pattern * qty)

    return ''.join(stack)


class Test(unittest.TestCase):
    def test_00(self):
        assert decompress_braces("2{q}3{tu}v") == "qqtututuv"

    def test_01(self):
        assert decompress_braces("ch3{ao}") == "chaoaoao"

    def test_02(self):
        assert decompress_braces("2{y3{o}}s") == "yoooyooos"

    def test_03(self):
        assert decompress_braces("z3{a2{xy}b}") == "zaxyxybaxyxybaxyxyb"

    def test_04(self):
        assert decompress_braces("2{3{r4{e}r}io}") == "reeeerreeeerreeeerioreeeerreeeerreeeerio"

    def test_05(self):
        assert decompress_braces("go3{spinn2{ing}s}") == "gospinningingsspinningingsspinningings"

    def test_06(self):
        assert decompress_braces("2{l2{if}azu}l") == "lififazulififazul"

    def test_07(self):
        assert decompress_braces("3{al4{ec}2{icia}}") == "alececececiciaiciaalececececiciaiciaalececececiciaicia"


if __name__ == "__main__":
    unittest.main()
