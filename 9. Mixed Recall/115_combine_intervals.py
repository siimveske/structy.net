"""
combine intervals
Write a function, combine_intervals, that takes in a list of intervals as an argument. Each interval is a tuple containing a pair of numbers representing a start and end time. Your function should combine overlapping intervals and return a list containing the combined intervals.

For example:

Given two intervals:

(1, 4) and (3, 7)

The intervals overlap and
should be combined into:

(1, 7)
You may return the combined intervals in any order.

You can assume that the input list contains at least one interval and all intervals are valid with start < end.

test_00
intervals = [
  (1, 4),
  (12, 15),
  (3, 7),
  (8, 13),
]
combine_intervals(intervals)
# -> [ (1, 7), (8, 15) ]
test_01
intervals = [
  (6, 8),
  (2, 9),
  (10, 12),
  (20, 24),
]
combine_intervals(intervals)
# -> [ (2, 9), (10, 12), (20, 24) ]
test_02
intervals = [
  (3, 7),
  (5, 8),
  (1, 5),
]
combine_intervals(intervals)
# -> [ (1, 8) ]
test_03
intervals = [
  (3, 7),
  (10, 13),
  (5, 8),
  (27, 31),
  (1, 5),
  (12, 16),
  (20, 22),
]
combine_intervals(intervals)
# -> [ (1, 8), (10, 16), (20, 22), (27, 31) ]
test_04
intervals = [
  (3, 7),
  (10, 13),
  (5, 8),
  (27, 31),
  (1, 5),
  (12, 16),
  (20, 32),
]
combine_intervals(intervals)
# -> [ (1, 8), (10, 16), (20, 32) ]
test_05
intervals = [
  (64, 70),
  (50, 55),
  (62, 65),
  (12, 50),
  (72, 300000),
]
combine_intervals(intervals)
# -> [ (12, 55), (62, 70), (72, 300000) ]
"""
