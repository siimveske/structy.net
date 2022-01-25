"""
safe cracking
Oh-no! You forgot the number combination that unlocks your safe. Luckily, you knew that you'd be forgetful so you previously wrote down a bunch of hints that can be used to determine the correct combination. Each hint is a pair of numbers 'x, y' that indicates you must enter digit 'x' before 'y' (but not necessarily immediately before y).

The keypad on the safe has digits 0-9. You can assume that the hints will generate exactly one working combination and that a digit can occur zero or one time in the answer.

Write a function, safe_cracking, that takes in a list of hints as an argument and determines the combination that will unlock the safe. The function should return a string representing the combination.

test_00:
safe_cracking([
  (7, 1),
  (1, 8),
  (7, 8),
]) # -> '718'
test_01:
safe_cracking([
  (3, 1),
  (4, 7),
  (5, 9),
  (4, 3),
  (7, 3),
  (3, 5),
  (9, 1),
]) # -> '473591'
test_02:
safe_cracking([
  (2, 5),
  (8, 6),
  (0, 6),
  (6, 2),
  (0, 8),
  (2, 3),
  (3, 5),
  (6, 5),
]) # -> '086235'
test_03:
safe_cracking([
  (0, 1),
  (6, 0),
  (1, 8),
]) # -> '6018'
test_04:
safe_cracking([
  (8, 9),
  (4, 2),
  (8, 2),
  (3, 8),
  (2, 9),
  (4, 9),
  (8, 4),
]) # -> '38429'
"""
