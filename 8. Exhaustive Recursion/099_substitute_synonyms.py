"""
--- Substituting synonyms ---
Write a function, substituting_synonyms, that takes in a sentence and a dictionary as arguments. The dictionary contains words as keys whose values are arrays containing synonyms. The function should return an array containing all possible sentences that can be formed by substituting words of the sentence with their synonyms.

You may return the possible sentences in any order, as long as you return all of them.
"""
import unittest


def substitute_synonyms(sentence, synonyms):
    sentence = sentence.split()
    raw_result = _substitute_synonyms(sentence, synonyms)
    result = [' '.join(i) for i in raw_result]

    return result


def _substitute_synonyms(sentence, synonyms):
    if not sentence:
        return [[]]

    result = []
    current = sentence[0]
    subarrays = _substitute_synonyms(sentence[1:], synonyms)

    if current in synonyms:
        for synonym in synonyms[current]:
            for suffix in subarrays:
                result.append([synonym] + suffix)
    else:
        for suffix in subarrays:
            result.append([current] + suffix)

    return result


class Test(unittest.TestCase):
    def test_00(self):
        sentence = "follow the yellow brick road"
        synonyms = {
            "follow": ["chase", "pursue"],
            "yellow": ["gold", "amber", "lemon"],
        }

        assert substitute_synonyms(sentence, synonyms) == [
            'chase the gold brick road',
            'chase the amber brick road',
            'chase the lemon brick road',
            'pursue the gold brick road',
            'pursue the amber brick road',
            'pursue the lemon brick road'
        ]

    def test_01(self):
        sentence = "I think it's gonna be a long long time"
        synonyms = {
            "think": ["believe", "reckon"],
            "long": ["lengthy", "prolonged"],
        }

        assert substitute_synonyms(sentence, synonyms) == [
            "I believe it's gonna be a lengthy lengthy time",
            "I believe it's gonna be a lengthy prolonged time",
            "I believe it's gonna be a prolonged lengthy time",
            "I believe it's gonna be a prolonged prolonged time",
            "I reckon it's gonna be a lengthy lengthy time",
            "I reckon it's gonna be a lengthy prolonged time",
            "I reckon it's gonna be a prolonged lengthy time",
            "I reckon it's gonna be a prolonged prolonged time"
        ]

    def test_02(self):
        sentence = "palms sweaty knees weak arms heavy"
        synonyms = {
            "palms": ["hands", "fists"],
            "heavy": ["weighty", "hefty", "burdensome"],
            "weak": ["fragile", "feeble", "frail", "sickly"],
        }

        assert substitute_synonyms(sentence, synonyms) == [
            'hands sweaty knees fragile arms weighty',
            'hands sweaty knees fragile arms hefty',
            'hands sweaty knees fragile arms burdensome',
            'hands sweaty knees feeble arms weighty',
            'hands sweaty knees feeble arms hefty',
            'hands sweaty knees feeble arms burdensome',
            'hands sweaty knees frail arms weighty',
            'hands sweaty knees frail arms hefty',
            'hands sweaty knees frail arms burdensome',
            'hands sweaty knees sickly arms weighty',
            'hands sweaty knees sickly arms hefty',
            'hands sweaty knees sickly arms burdensome',
            'fists sweaty knees fragile arms weighty',
            'fists sweaty knees fragile arms hefty',
            'fists sweaty knees fragile arms burdensome',
            'fists sweaty knees feeble arms weighty',
            'fists sweaty knees feeble arms hefty',
            'fists sweaty knees feeble arms burdensome',
            'fists sweaty knees frail arms weighty',
            'fists sweaty knees frail arms hefty',
            'fists sweaty knees frail arms burdensome',
            'fists sweaty knees sickly arms weighty',
            'fists sweaty knees sickly arms hefty',
            'fists sweaty knees sickly arms burdensome'
        ]


if __name__ == "__main__":
    unittest.main()
