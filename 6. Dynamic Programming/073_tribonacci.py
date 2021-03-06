import unittest

"""
tribonacci
Write a function tribonacci that takes in a number argument, n, and returns the n-th number of the Tribonacci sequence.
The 0-th and 1-st numbers of the sequence are both 0.
The 2-nd number of the sequence is 1.
To generate further numbers of the sequence, calculate the sum of previous three numbers.
Solve this recursively.
"""


def tribonacci(n):
    solutions = {0: 0, 1: 0, 2: 1}
    result = calculate(n, solutions)
    return result


def calculate(n, solutions):
    if n in solutions:
        return solutions[n]

    solutions[n] = \
        calculate(n - 1, solutions) + \
        calculate(n - 2, solutions) + \
        calculate(n - 3, solutions)

    return solutions[n]


class Test(unittest.TestCase):
    def test_00(self):
        assert tribonacci(0) == 0

    def test_01(self):
        assert tribonacci(1) == 0

    def test_02(self):
        assert tribonacci(2) == 1

    def test_03(self):
        assert tribonacci(5) == 4

    def test_04(self):
        assert tribonacci(7) == 13

    def test_05(self):
        assert tribonacci(14) == 927

    def test_06(self):
        assert tribonacci(20) == 35890

    def test_07(self):
        assert tribonacci(37) == 1132436852


if __name__ == "__main__":
    unittest.main()
