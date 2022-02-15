"""
--- Detect dictionary ---
Write a function, detectDictionary, that takes in a dictionary of words and an alphabet string. The function should return a boolean indicating whether or not all words of the dictionary are lexically-ordered according to the alphabet.

You can assume that all characters are lowercase a-z.

You can assume that the alphabet contains all 26 letters.
"""
import unittest


def detect_dictionary(dictionary, alphabet):
    mapping = {}
    for letter_idx, letter in enumerate(alphabet):
        mapping[letter] = letter_idx

    for word_idx in range(len(dictionary) - 1):
        current_word = dictionary[word_idx]
        next_word = dictionary[word_idx + 1]

        for char_idx, char1 in enumerate(current_word):
            try:
                char2 = next_word[char_idx]
                if mapping[char1] > mapping[char2]:
                    return False
            except IndexError:
                return False

    return True


class Test(unittest.TestCase):
    def test_00(self):
        dictionary = ["zoo", "tick", "tack", "door"]
        alphabet = "ghzstijbacdopnfklmeqrxyuvw"
        detect_dictionary(dictionary, alphabet) == True

    def test_01(self):
        dictionary = ["zoo", "tack", "tick", "door"]
        alphabet = "ghzstijbacdopnfklmeqrxyuvw"
        detect_dictionary(dictionary, alphabet) == False

    def test_02(self):
        dictionary = ["zoos", "zoo", "tick", "tack", "door"]
        alphabet = "ghzstijbacdopnfklmeqrxyuvw"
        detect_dictionary(dictionary, alphabet) == False

    def test_03(self):
        dictionary = ["miles", "milestone", "proper", "process", "goal"]
        alphabet = "mnoijpqrshkltabcdefguvwzxy"
        detect_dictionary(dictionary, alphabet) == True

    def test_04(self):
        dictionary = ["miles", "milestone", "pint", "proper", "process", "goal"]
        alphabet = "mnoijpqrshkltabcdefguvwzxy"
        detect_dictionary(dictionary, alphabet) == True

    def test_05(self):
        dictionary = ["miles", "milestone", "pint", "proper", "process", "goal", "apple"]
        alphabet = "mnoijpqrshkltabcdefguvwzxy"
        detect_dictionary(dictionary, alphabet) == False


if __name__ == "__main__":
    unittest.main()
