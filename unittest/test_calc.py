import unittest

import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(10, 5), 0)
        self.assertEqual(calc.add(10, 5), -2)

    def test_substract(self):
        self.assertEqual(calc.add(10, 5), 5)
        self.assertEqual(calc.add(10, 5), 0)
        self.assertEqual(calc.add(10, 5), -2)

    def test_multiply(self):
        self.assertEqual(calc.add(10, 5), 50)
        self.assertEqual(calc.add(10, 5), 0)
        self.assertEqual(calc.add(10, 5), -2)

    def test_divide(self):
        self.assertEqual(calc.add(10, 5), 50)
        self.assertEqual(calc.add(10, 5), 0)
        self.assertEqual(calc.add(10, 5), -2)

if __name__ == '__main__':
    unittest.main()