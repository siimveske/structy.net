"""
--- Combine intervals ---
Write a function, combine_intervals, that takes in a list of intervals as an argument. Each interval is a tuple containing a pair of numbers representing a start and end time. Your function should combine overlapping intervals and return a list containing the combined intervals.

For example:

Given two intervals:

(1, 4) and (3, 7)

The intervals overlap and
should be combined into:

(1, 7)
You may return the combined intervals in any order.

You can assume that the input list contains at least one interval and all intervals are valid with start < end.
"""
import unittest


def combine_intervals(intervals):
    sorted_intervals = sorted(intervals)
    result = [sorted_intervals[0]]

    for idx in range(1, len(sorted_intervals)):
        last_start, last_end = result[-1]
        current_start, current_end = sorted_intervals[idx]
        if current_start >= last_start and current_end <= last_end:
            continue
        if current_start >= last_start and current_start <= last_end:
            result.pop()
            result.append((last_start, current_end))
            continue
        if current_start > last_end:
            result.append((current_start, current_end))

    return result


class Test(unittest.TestCase):
    def test_00(self):
        intervals = [
            (1, 4),
            (12, 15),
            (3, 7),
            (8, 13),
        ]
        assert combine_intervals(intervals) == [(1, 7), (8, 15)]

    def test_01(self):
        intervals = [
            (6, 8),
            (2, 9),
            (10, 12),
            (20, 24),
        ]
        assert combine_intervals(intervals) == [(2, 9), (10, 12), (20, 24)]

    def test_02(self):
        intervals = [
            (3, 7),
            (5, 8),
            (1, 5),
        ]
        assert combine_intervals(intervals) == [(1, 8)]

    def test_03(self):
        intervals = [
            (3, 7),
            (10, 13),
            (5, 8),
            (27, 31),
            (1, 5),
            (12, 16),
            (20, 22),
        ]
        assert combine_intervals(intervals) == [(1, 8), (10, 16), (20, 22), (27, 31)]

    def test_04(self):
        intervals = [
            (3, 7),
            (10, 13),
            (5, 8),
            (27, 31),
            (1, 5),
            (12, 16),
            (20, 32),
        ]
        assert combine_intervals(intervals) == [(1, 8), (10, 16), (20, 32)]

    def test_05(self):
        intervals = [
            (64, 70),
            (50, 55),
            (62, 65),
            (12, 50),
            (72, 300000),
        ]
        assert combine_intervals(intervals) == [(12, 55), (62, 70), (72, 300000)]


if __name__ == "__main__":
    unittest.main()
