import unittest


def greet(s):
    return f"hey {s}"


class TestGreet(unittest.TestCase):
    def test_01(self):
        self.assertEqual(greet("alvin"), "hey alvin")

    def test_02(self):
        self.assertEqual(greet("jason"), "hey jason")

    def test_03(self):
        self.assertEqual(greet("how now brown cow"), "hey how now brown cow")


if __name__ == "__main__":
    unittest.main()
