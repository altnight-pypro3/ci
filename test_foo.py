import unittest

import foo


class SimpleTest(unittest.TestCase):
    """割り算する関数をテストする。
    """
    def test1(self):
        self.assertEqual(foo.divide(2, 2), 1)

    def test2(self):
        self.assertEqual(foo.divide(0, 1), 0)


if __name__ == "__main__":
    unittest.main()
