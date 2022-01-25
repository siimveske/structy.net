import math
import unittest


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


class Test(unittest.TestCase):
    def test_00(self):
        assert is_prime(2) == True

    def test_01(self):
        assert is_prime(3) == True

    def test_02(self):
        assert is_prime(4) == False

    def test_03(self):
        assert is_prime(5) == True

    def test_04(self):
        assert is_prime(6) == False

    def test_05(self):
        assert is_prime(7) == True

    def test_06(self):
        assert is_prime(8) == False

    def test_07(self):
        assert is_prime(25) == False

    def test_08(self):
        assert is_prime(31) == True

    def test_09(self):
        assert is_prime(2017) == True

    def test_10(self):
        assert is_prime(2048) == False

    def test_11(self):
        assert is_prime(1) == False

    def test_12(self):
        assert is_prime(713) == False


if __name__ == "__main__":
    unittest.main()
