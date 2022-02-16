"""
--- Token transform ---
Write a function, token_transform, that takes in a dictionary of tokens and a string. In the dictionary, the replacement values for a token may reference other tokens. The function should return a new string where tokens are replaced with their fully evaluated string values.

Tokens are enclosed in a pair of '$'.

You may assume that their are no circular token dependencies.
"""
import unittest


def token_transform(s, tokens):
    result = []
    i = 0
    j = 1

    while i < len(s):
        if s[i] == '$':
            while s[j] != '$':
                j += 1
            key = s[i:j + 1]
            value = token_transform(tokens[key], tokens)
            result.append(value)
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
            '$LOCATION$': '$ANIMAL$ park',
            '$ANIMAL$': 'dog',
        }
        assert token_transform('Walk the $ANIMAL$ in the $LOCATION$!', tokens) == 'Walk the dog in the dog park!'

    def test_01(self):
        tokens = {
            '$ADJECTIVE_1$': "quick",
            '$ADJECTIVE_2$': "eager",
            '$ADVERBS$': "$ADJECTIVE_1$ly and $ADJECTIVE_2$ly",
            '$VERB$': "hopped $DIRECTION$",
            '$DIRECTION$': "North",
        }
        assert token_transform("the $ADJECTIVE_1$ fox $ADVERBS$ $VERB$ward", tokens) == 'the quick fox quickly and eagerly hopped Northward'

    def test_02(self):
        tokens = {
            '$B$': "epicly $C$",
            '$A$': "pretty $B$ problem $D$",
            '$D$': "we have",
            '$C$': "clever",
        }
        assert token_transform("What a $A$ here!", tokens) == 'What a pretty epicly clever problem we have here!'

    def test_03(self):
        tokens = {
            '$1$': "a$2$",
            '$2$': "b$3$",
            '$3$': "c$4$",
            '$4$': "d$5$",
            '$5$': "e$6$",
            '$6$': "f!",
        }
        assert token_transform("$1$ $1$ $1$ $1$ $1$ $1$ $4$ $4$", tokens) == 'abcdef! abcdef! abcdef! abcdef! abcdef! abcdef! def! def!'

    def test_04(self):
        tokens = {
            '$0$': "$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$",
            '$1$': "$2$$2$$2$$2$$2$$2$$2$$2$$2$",
            '$2$': "$3$$3$$3$$3$$3$$3$$3$",
            '$3$': "$4$$4$$4$$4$$4$$4$",
            '$4$': "$5$$5$$5$$5$$5$",
            '$5$': "$6$$6$$6$$6$",
            '$6$': "$7$$7$$7$",
            '$7$': "$8$$8$",
            '$8$': "",
        }
        assert token_transform("z$0$z$0$z$0$z$0$z$0$z$0$z", tokens) == 'zzzzzzz'


if __name__ == "__main__":
    unittest.main()
