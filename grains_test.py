import unittest

from grains import on_square, total_after
from grains import on_square_norec, total_after_norec


class GrainsTest(unittest.TestCase):
    def test_square_0(self):
        with self.assertRaises(IndexError):
            on_square(0)
            total_after(0)

    def test_square_1(self):
        self.assertEqual(1, on_square(1))
        self.assertEqual(1, total_after(1))

    def test_square_2(self):
        self.assertEqual(2, on_square(2))
        self.assertEqual(3, total_after(2))

    def test_square_3(self):
        self.assertEqual(4, on_square(3))
        self.assertEqual(7, total_after(3))

    def test_square_4(self):
        self.assertEqual(8, on_square(4))
        self.assertEqual(15, total_after(4))

    def test_square_16(self):
        self.assertEqual(32768, on_square(16))
        self.assertEqual(65535, total_after(16))

    def test_square_32(self):
        self.assertEqual(2147483648, on_square(32))
        self.assertEqual(4294967295, total_after(32))

    def test_square_64(self):
        self.assertEqual(9223372036854775808, on_square(64))
        self.assertEqual(18446744073709551615, total_after(64))

    def test_square_65(self):
        with self.assertRaises(IndexError):
            on_square(65)
            total_after(65)

    def test_square_norec(self):
        # 1
        self.assertEqual(1, on_square_norec(1))
        self.assertEqual(1, total_after_norec(1))
        # 64
        self.assertEqual(9223372036854775808, on_square_norec(64))
        self.assertEqual(18446744073709551615, total_after_norec(64))

        # beyond
        self.assertEqual(18446744073709551616L, on_square_norec(65))
        self.assertEqual(36893488147419103231L, total_after_norec(65))

        # ~20s
        self.assertNotEqual(0, on_square_norec(int(3e5)))
        self.assertNotEqual(0, on_square_norec(int(3e5)))
        self.assertNotEqual(0, total_after_norec(int(3e5)))
        self.assertNotEqual(0, total_after_norec(int(3e5)))


if __name__ == '__main__':
    unittest.main()
