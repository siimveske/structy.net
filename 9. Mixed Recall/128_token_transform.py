"""
token transform
Write a function, token_transform, that takes in a dictionary of tokens and a string. In the dictionary, the replacement values for a token may reference other tokens. The function should return a new string where tokens are replaced with their fully evaluated string values.

Tokens are enclosed in a pair of '$'.

You may assume that their are no circular token dependencies.

test_00:
tokens = {
  '$LOCATION$': '$ANIMAL$ park',
  '$ANIMAL$': 'dog',
}
token_transform('Walk the $ANIMAL$ in the $LOCATION$!', tokens)
# -> 'Walk the dog in the dog park!'
test_01:
tokens = {
  '$ADJECTIVE_1$': "quick",
  '$ADJECTIVE_2$': "eager",
  '$ADVERBS$': "$ADJECTIVE_1$ly and $ADJECTIVE_2$ly",
  '$VERB$': "hopped $DIRECTION$",
  '$DIRECTION$': "North",
}
token_transform("the $ADJECTIVE_1$ fox $ADVERBS$ $VERB$ward", tokens)
# -> 'the quick fox quickly and eagerly hopped Northward'
test_02:
tokens = {
  '$B$': "epicly $C$",
  '$A$': "pretty $B$ problem $D$",
  '$D$': "we have",
  '$C$': "clever",
}
token_transform("What a $A$ here!", tokens)
# -> 'What a pretty epicly clever problem we have here!'
test_03:
tokens = {
  '$1$': "a$2$",
  '$2$': "b$3$",
  '$3$': "c$4$",
  '$4$': "d$5$",
  '$5$': "e$6$",
  '$6$': "f!",
}
token_transform("$1$ $1$ $1$ $1$ $1$ $1$ $4$ $4$", tokens)
# -> 'abcdef! abcdef! abcdef! abcdef! abcdef! abcdef! def! def!'
test_04:
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
token_transform("z$0$z$0$z$0$z$0$z$0$z$0$z", tokens)
# -> 'zzzzzzz'
"""
