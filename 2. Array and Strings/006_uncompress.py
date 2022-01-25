"""
--- uncompress ---
Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:

<number><char>
for example, '2c' or '3a'.

The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.
"""

import unittest


def uncompress(s):
    result = []

    count = ''
    for letter in s:
        if letter.isdigit():
            count += letter
        else:
            result.append(letter * int(count))
            count = ''

    return ''.join(result)


class Test(unittest.TestCase):
    def test_00(self):
        assert uncompress("2c3a1t") == 'ccaaat'

    def test_01(self):
        assert uncompress("4s2b") == 'ssssbb'

    def test_02(self):
        assert uncompress("2p1o5p") == 'ppoppppp'

    def test_03(self):
        assert uncompress("3n12e2z") == 'nnneeeeeeeeeeeezz'

    def test_04(self):
        assert uncompress("127y") == 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'


if __name__ == "__main__":
    unittest.main()
