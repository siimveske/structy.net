"""
string search
Write a function, string_search, that takes in a grid of letters and a string as arguments. The function should return a boolean indicating whether or not the string can be found in the grid as a path by connecting horizontal or vertical positions. The path can begin at any position, but you cannot reuse a position more than once in the path.

You can assume that all letters are lowercase and alphabetic.

test_00:
grid = [
  ['e', 'y', 'h', 'i', 'j'],
  ['q', 'x', 'e', 'r', 'p'],
  ['r', 'o', 'l', 'l', 'n'],
  ['p', 'r', 'x', 'o', 'h'],
  ['a', 'a', 'm', 'c', 'm']
]
string_search(grid, 'hello') # -> True
test_01:
grid = [
  ['e', 'y', 'h', 'i', 'j'],
  ['q', 'x', 'e', 'r', 'p'],
  ['r', 'o', 'l', 'l', 'n'],
  ['p', 'r', 'x', 'o', 'h'],
  ['a', 'a', 'm', 'c', 'm']
]
string_search(grid, 'proxy') # -> True
test_02:
grid = [
  ['e', 'y', 'h', 'i', 'j'],
  ['q', 'x', 'e', 'r', 'p'],
  ['r', 'o', 'l', 'l', 'n'],
  ['p', 'r', 'x', 'o', 'h'],
  ['a', 'a', 'm', 'c', 'm']
]
string_search(grid, 'rolling') # -> False
test_03:
grid = [
  ['e', 'y', 'h', 'i', 'j'],
  ['q', 'x', 'e', 'r', 'p'],
  ['r', 'o', 'l', 'l', 'n'],
  ['p', 'r', 'x', 'o', 'h'],
  ['a', 'a', 'm', 'z', 'm']
]
string_search(grid, 'zoo') # -> False
test_04:
grid = [
  ['q', 'w', 'h', 'i', 'j'],
  ['q', 'e', 'r', 'o', 'p'],
  ['h', 'y', 't', 'x', 'z'],
  ['k', 'o', 'm', 'o', 'p']
]
string_search(grid, 'qwerty') # -> True
test_05:
grid = [
  [ 'f', 'd', 'i', 'e', 'l', 'u', 'j', 't', 'q', 'v', 'o', 'p' ],
  [ 'o', 'p', 'b', 'e', 'm', 'w', 'm', 'l', 'h', 'j', 's', 'v' ],
  [ 'g', 'b', 's', 'm', 'i', 'w', 'w', 'h', 'l', 'm', 'l', 'n' ],
  [ 'a', 'l', 's', 'k', 'p', 'c', 't', 'u', 'v', 'b', 'c', 'm' ],
  [ 'm', 't', 'c', 'k', 'e', 'n', 'r', 'b', 'a', 'z', 'l', 'c' ],
  [ 'q', 'm', 'a', 'p', 'a', 'p', 'i', 'i', 'u', 't', 'z', 'z' ],
  [ 'd', 'u', 'z', 'o', 'e', 'r', 'a', 't', 't', 'c', 'q', 'k' ],
  [ 'f', 'u', 'z', 'g', 'c', 'i', 'k', 'v', 'o', 'f', 's', 'w' ],
  [ 'p', 'h', 'u', 'i', 'k', 'c', 'v', 'v', 'h', 'q', 'v', 'i' ],
  [ 'l', 'q', 'w', 'f', 'y', 'g', 'w', 'f', 'a', 'u', 'x', 'q' ]
]
string_search(grid, 'paprika') # -> True
test_06:
grid = [
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 'x', 'x' ],
    [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 'x', 'h' ],
]
string_search(grid, 'ssssssssssh') # -> False
"""
