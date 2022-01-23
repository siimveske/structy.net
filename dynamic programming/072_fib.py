import unittest


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
