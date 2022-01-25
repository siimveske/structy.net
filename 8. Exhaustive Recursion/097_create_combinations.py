"""
create combinations
Write a function, create_combinations, that takes in a list and a length as arguments. The function should return a 2D list representing all of the combinations of the specifized length.

The items within the combinations and the combinations themselves may be returned in any order.

You may assume that the input list contains unique elements and 1 <= k <= len(items).

test_00:
create_combinations(["a", "b", "c"], 2); # ->
# [
#   [ 'a', 'b' ],
#   [ 'a', 'c' ],
#   [ 'b', 'c' ]
# ]
test_01:
create_combinations(["q", "r", "s", "t"], 2); # ->
# [
#   [ 'q', 'r' ],
#   [ 'q', 's' ],
#   [ 'q', 't' ],
#   [ 'r', 's' ],
#   [ 'r', 't' ],
#   [ 's', 't' ]
# ]
test_02:
create_combinations(['q', 'r', 's', 't'], 3)); # ->
# [
#   [ 'q', 'r', 's' ],
#   [ 'q', 'r', 't' ],
#   [ 'q', 's', 't' ],
#   [ 'r', 's', 't' ]
# ]
test_03:
create_combinations([1, 28, 94], 3); # ->
# [
#   [ 1, 28, 94 ]
# ]
"""
