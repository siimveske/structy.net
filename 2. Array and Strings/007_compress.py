"""
--- Compress ---
Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'
You can assume that the input only contains alphabetic characters.
"""
import unittest


def store_result(s, head, tail, container):
    qty = head - tail
    item = s[tail]
    if qty > 1:
        container.append(f"{qty}{item}")
    else:
        container.append(item)


def compress(s):
    result = []
    tail = 0
    head = 0
    for character in s:
        if s[tail] != s[head]:
            store_result(s, head, tail, result)
            tail = head
        head += 1
    store_result(s, head, tail, result)

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
