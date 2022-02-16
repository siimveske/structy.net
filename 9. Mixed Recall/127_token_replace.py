"""
--- Token replace ---
Write a function, token_replace, that takes in a dictionary of tokens and a string. The function should return a new string where tokens are replaced.

Tokens are enclosed in a pair of '$'. You can assume that the input string is properly formatted. Tokens should be replaced from left to right in the string (see test_05).
"""
import unittest


def token_replace(s, tokens):
    result = []
    i = 0
    j = 1

    while i < len(s):
        if s[i] == '$':
            while s[j] != '$':
                j += 1
            key = s[i:j + 1]
            result.append(tokens[key])
            i = j + 1
            j = i + 1
        else:
            result.append(s[i])
            i += 1
            j += 1

    return ''.join(result)


class Test(unittest.TestCase):
    def test_00(self):
        tokens = {
            '$LOCATION$': 'park',
            '$ANIMAL$': 'dog',
        }
        assert token_replace('Walk the $ANIMAL$ in the $LOCATION$!', tokens) == 'Walk the dog in the park!'

    def test_01(self):
        tokens = {
            '$ADJECTIVE$': 'quick',
            '$VERB$': 'hopped',
            '$DIRECTION$': 'North'
        }
        assert token_replace('the $ADJECTIVE$ fox $VERB$ $ADJECTIVE$ly $DIRECTION$ward', tokens) == 'the quick fox hopped quickly Northward'

    def test_02(self):
        tokens = {
            '$greeting$': 'hey programmer',
        }
        assert token_replace('his greeting is always $greeting$.', tokens) == 'his greeting is always hey programmer.'

    def test_03(self):
        tokens = {
            '$A$': 'lions',
            '$B$': 'tigers',
            '$C$': 'bears',
        }
        assert token_replace('$A$$B$$C$, oh my.', tokens) == 'lionstigersbears, oh my.'

    def test_04(self):
        tokens = {
            '$A$': 'lions',
            '$B$': 'tigers',
            '$C$': 'bears',
        }
        assert token_replace('$B$', tokens) == 'tigers'

    def test_05(self):
        tokens = {
            '$second$': 'beta',
            '$first$': 'alpha',
            '$third$': 'gamma',
        }
        assert token_replace('$first$second$third$', tokens) == 'alphasecondgamma'


if __name__ == "__main__":
    unittest.main()
