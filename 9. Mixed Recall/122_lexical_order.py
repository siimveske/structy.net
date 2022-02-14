"""
--- Lexical order ---
Write a function, lexical_order, that takes in 2 words and an alphabet string as an argument. The function should return True if the first word should appear before the second word if lexically-ordered according to the given alphabet order. If the second word should appear first, then return False.

Note that the alphabet string may be any arbitrary string.

Intuitively, Lexical Order is like "dictionary" order:

You can assume that all characters are lowercase a-z.

You can assume that the alphabet contains all 26 letters.
"""
import unittest


def lexical_order(word_1, word_2, alphabet):
    mapping = {}
    for idx, letter in enumerate(alphabet):
        mapping[letter] = idx

    for idx, letter1 in enumerate(word_1):
        try:
            letter2 = word_2[idx]
            if mapping[letter1] < mapping[letter2]:
                return True
            elif mapping[letter1] > mapping[letter2]:
                return False
        except IndexError:
            return False

    return True


class Test(unittest.TestCase):
    def test_00(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        assert lexical_order("apple", "dock", alphabet) == True

    def test_01(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        assert lexical_order("apple", "ample", alphabet) == False

    def test_02(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        assert lexical_order("app", "application", alphabet) == True

    def test_03(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        assert lexical_order("backs", "backdoor", alphabet) == False

    def test_04(self):
        alphabet = "ghzstijbacdopnfklmeqrxyuvw"
        assert lexical_order("zoo", "dinner", alphabet) == True

    def test_05(self):
        alphabet = "ghzstijbacdopnfklmeqrxyuvw"
        assert lexical_order("leaper", "leap", alphabet) == False

    def test_06(self):
        alphabet = "ghzstijbacdopnfklmeqrxyuvw"
        assert lexical_order("backs", "backdoor", alphabet) == True

    def test_07(self):
        alphabet = "ghzstijbacdopnfklmeqrxyuvw"
        assert lexical_order("semper", "semper", alphabet) == True


if __name__ == "__main__":
    unittest.main()
