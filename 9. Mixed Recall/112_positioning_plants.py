"""
positioning plants
You've been hired to plant flowers in a garden with n different positions. There are m different flower types. The prices of flowers types vary depending on which position they are planted. Your bosses are picky, they tell you to never plant two of the same flower type right next to each other. What is the minimum cost we need to plant a flower in each position of the garden?

Write a function, positioningPlants, that takes in a 2D list with dimensions n * m. Each row of the list represents the costs of the flower types at that position. This means that costs[i][j] represents the cost of planting flower type j at position i. For example:

Given these costs,

costs = [
  [4, 3, 7],
  [6, 1, 9],
  [2, 5, 3]
]

The costs of plants at position 1 are $6, $1, and $9.
The cost of planting flower type 0 at position 1 is $6.
The cost of planting flower type 2 at position 1 is $9.
The function should return the minimum cost of planting flowers without placing the same flower type in adjacent positions.

test_00:
positioning_plants([
  [4, 3, 7],
  [6, 1, 9],
  [2, 5, 3]
]) # -> 7, by doing 4 + 1 + 2.
test_01:
positioning_plants([
  [12, 14, 5],
  [6, 3, 2]
]) # -> 8
test_02:
positioning_plants([
  [12, 14, 5],
  [6, 3, 2],
  [4, 2, 7],
  [4, 8, 4],
  [1, 13, 5],
  [8, 6, 7],
]) # -> 23
test_03:
positioning_plants([
  [12, 14, 5, 13],
  [6, 3, 20, 3],
  [24, 12, 7, 2],
  [4, 80, 45, 3],
  [104, 13, 5, 14],
  [38, 19, 7, 6],
  [12, 2, 1, 2],
]) # -> 26
test_04:
positioning_plants([
  [12, 14, 50, 12],
  [6, 3, 20, 3],
  [24, 12, 7, 2],
  [4, 80, 45, 3],
  [104, 13, 5, 14],
  [38, 19, 7, 6],
  [1, 20, 1, 2],
  [13, 12, 5, 13],
  [60, 32, 20, 3],
  [24, 12, 7, 2],
  [4, 80, 44, 1],
  [104, 13, 5, 14],
  [38, 19, 76, 6],
  [12, 23, 12, 20],
  [1, 3, 1, 1],
  [1, 2, 12, 5],
]) # -> 74
test_05:
positioning_plants([
  [12, 14, 50, 12, 13],
  [6, 3, 20, 3, 16],
  [24, 12, 7, 2, 74],
  [4, 80, 45, 3, 100],
  [104, 13, 5, 14, 3],
  [38, 19, 7, 6, 24],
  [1, 20, 1, 2, 31],
  [13, 12, 5, 13, 9],
  [60, 32, 20, 3, 2],
  [24, 12, 7, 2, 42],
  [4, 80, 44, 1, 23],
  [104, 13, 5, 14, 28],
  [38, 19, 76, 6, 12],
  [12, 23, 12, 20, 13],
  [1, 3, 1, 1, 50],
  [1, 2, 12, 5, 36],
  [6, 2, 3, 12, 20],
  [4, 6, 4, 11, 15],
]) # -> 75
"""
