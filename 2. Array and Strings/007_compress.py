"""
--- Compress ---
Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'
You can assume that the input only contains alphabetic characters.
"""
import unittest


def store_result(string, start, end, container):
    qty = end - start
    item = string[start]
    if qty > 1:
        container.append(f"{qty}{item}")
    else:
        container.append(item)


def compress(string):
    result = []
    start = 0
    end = 0
    str_length = len(string)
    while end < str_length:
        if string[start] == string[end]:
            end += 1
        else:
            store_result(string, start, end, result)
            start = end
    store_result(string, start, end, result)

    return ''.join(result)


class Test(unittest.TestCase):
    def test_00(self):
        assert compress('ccaaatsss') == '2c3at3s'

    def test_01(self):
        assert compress('ssssbbz') == '4s2bz'

    def test_02(self):
        assert compress('ppoppppp') == '2po5p'

    def test_03(self):
        assert compress('nnneeeeeeeeeeeezz') == '3n12e2z'

    def test_04(self):
        assert compress(
            'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
        ) == '127y'


if __name__ == "__main__":
    unittest.main()
