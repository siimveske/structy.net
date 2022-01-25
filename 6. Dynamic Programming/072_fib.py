import unittest

"""
--- fib ---
Write a function fib that takes in a number argument, n, and returns the n-th number of the Fibonacci sequence.

The 0-th number of the sequence is 0.
The 1-st number of the sequence is 1.

To generate further numbers of the sequence, calculate the sum of previous two numbers.

Solve this recursively.
"""


def fib(n):
    solutions = {0: 0, 1: 1}
    result = calculate(n, solutions)
    return result


def calculate(n, solutions):
    if n in solutions:
        return solutions[n]

    result = calculate(n - 1, solutions) + calculate(n - 2, solutions)
    solutions[n] = result

    return result


class Test(unittest.TestCase):
    def test_00(self):
        assert fib(0) == 0

    def test_01(self):
        assert fib(1) == 1

    def test_02(self):
        assert fib(2) == 1

    def test_03(self):
        assert fib(3) == 2

    def test_04(self):
        assert fib(4) == 3

    def test_05(self):
        assert fib(5) == 5

    def test_06(self):
        assert fib(35) == 9227465

    def test_07(self):
        assert fib(46) == 1836311903


if __name__ == "__main__":
    unittest.main()
