"""
--- Overlap subsequence ---
"""


import unittest


def overlap_subsequence(string_1, string_2):
    return calculate(string_1, string_2, (0, 0), {})


def calculate(string_1, string_2, idx, memo):
    idx1, idx2 = idx
    if idx in memo:
        return memo[idx]
    if idx1 >= len(string_1) or idx2 >= len(string_2):
        return 0

    result = 0
    if string_1[idx1] == string_2[idx2]:
        result += calculate(string_1, string_2, (idx1 + 1, idx2 + 1), memo) + 1
    else:
        left = calculate(string_1, string_2, (idx1 + 1, idx2), memo)
        right = calculate(string_1, string_2, (idx1, idx2 + 1), memo)
        result += max(left, right)

    memo[idx] = result
    return memo[idx]


class Test(unittest.TestCase):
    def test_00(self):
        assert overlap_subsequence("dogs", "daogt") == 3

    def test_01(self):
        assert overlap_subsequence("xcyats", "criaotsi") == 4

    def test_02(self):
        assert overlap_subsequence("xfeqortsver", "feeeuavoeqr") == 5

    def test_03(self):
        assert overlap_subsequence("kinfolklivemustache", "bespokekinfolksnackwave") == 11

    def test_04(self):
        assert overlap_subsequence(
            "mumblecorebeardleggingsauthenticunicorn",
            "succulentspughumblemeditationlocavore"
        ) == 15


if __name__ == "__main__":
    unittest.main()
