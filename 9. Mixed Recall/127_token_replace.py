"""
token replace
Write a function, token_replace, that takes in a dictionary of tokens and a string. The function should return a new string where tokens are replaced.

Tokens are enclosed in a pair of '$'. You can assume that the input string is properly formatted. Tokens should be replaced from left to right in the string (see test_05).

test_00:
tokens = {
  '$LOCATION$': 'park',
  '$ANIMAL$': 'dog',
}
token_replace('Walk the $ANIMAL$ in the $LOCATION$!', tokens)
# -> 'Walk the dog in the park!'
test_01:
tokens = {
  '$ADJECTIVE$': 'quick',
  '$VERB$': 'hopped',
  '$DIRECTION$': 'North'
}
token_replace('the $ADJECTIVE$ fox $VERB$ $ADJECTIVE$ly $DIRECTION$ward', tokens)
# -> 'the quick fox hopped quickly Northward'
test_02:
tokens = {
  '$greeting$': 'hey programmer',
}
token_replace('his greeting is always $greeting$.', tokens)
# -> 'his greeting is always hey programmer.'
test_03:
tokens = {
  '$A$': 'lions',
  '$B$': 'tigers',
  '$C$': 'bears',
}
token_replace('$A$$B$$C$, oh my.', tokens)
# -> 'lionstigersbears, oh my.'
test_04:
tokens = {
  '$A$': 'lions',
  '$B$': 'tigers',
  '$C$': 'bears',
}
token_replace('$B$', tokens)
# -> 'tigers'
test_05:
tokens = {
  '$second$': 'beta',
  '$first$': 'alpha',
  '$third$': 'gamma',
}
token_replace('$first$second$third$', tokens)
# -> 'alphasecondgamma'
"""
