from fraction import Fraction
import unittest

class FractionTestCase(unittest.TestCase):

    def test_init(self):
        fract1 = Fraction(2, 5)
        self.assertEqual(fract1.num, 2, "Normal test : numérateur")
        self.assertEqual(fract1.den, 5, "Normal test : dénominateur")
        self.assertEqual(fract1.total, 0.4, "Normal test : representation décimal")
        self.assertEqual(fract1.rest, 2, "Normal test : du reste")

        fract2 = Fraction(-3,-5)
        self.assertEqual(fract2.num, 3, "Normal test : numérateur")
        self.assertEqual(fract2.den, 5, "Normal test : dénominateur")
        self.assertEqual(fract2.total, 0.6, "Normal test : representation décimal")
        self.assertEqual(fract2.rest, 3, "Normal test : du reste")

        self.assertRaises(ZeroDivisionError, Fraction, 2, 0)

    def test_str(self):
        fract1 = Fraction(5, 10)
        self.assertEqual(fract1.__str__, "1/2", "Fraction(80, 168)")
        fract2 = Fraction(-80, 168)
        self.assertEqual(fract2.__str__, "-10/21", "Fraction(-80, 168)")

    def test_as_mixed_number(self):
        fract1 = Fraction(7, 5)
        self.assertEqual(fract1.as_mixed_number(), "1 et 2/5", "Fraction(7,5)")

        fract2 = Fraction(5, 5)
        self.assertEqual(fract2.as_mixed_number(), "1", "Fraction(5,5)")

        fract3 = Fraction(2, 5)
        self.assertEqual(fract3.as_mixed_number(), "2/5", "Fraction(2,5)")

    def test_add(self):
        fract1 = Fraction(3, 5)
        self.assertEqual(fract1.__add__(3, 5), "6/5", "fract1.__add__(3, 5)")
        self.assertEqual(fract1.__add__(-4, 5), "-1/5", "fract1.__add__(-4, 5)")
        self.assertEqual(fract1.__add__(0, 5), "3/5", "fract1.__add__(0, 5)")

        self.assertRaises(ZeroDivisionError, fract1.__add__, 2 , 0)

    def test_sub(self):
        fract1 = Fraction(4, 5)
        self.assertEqual(fract1.__sub__(3, 5), "1/5", "fract1.__sub__(3, 5)")
        self.assertEqual(fract1.__sub__(-4, 5), "8/5", "fract1.__sub__(-4, 5)")
        self.assertEqual(fract1.__sub__(0, 5), "4/5", "fract1.__sub__(0, 5)")

        self.assertRaises(ZeroDivisionError, fract1.__sub__, 2, 0)

    def test_mul(self):
        fract1 = Fraction(4, 5)
        self.assertEqual(fract1.__mul__(4, 6), "8/15", "fract1.__mul__(4, 6)")
        self.assertEqual(fract1.__mul__(-4, 6), "-8/15", "fract1.__mul__(-4, 6)")
        self.assertEqual(fract1.__mul__(0, 6), "0/1", "fract1.__mul__(0, 6)")

        self.assertRaises(ZeroDivisionError, fract1.__sub__, 2, 0)

    def test_truediv(self):
        fract1 = Fraction(4, 5)
        self.assertEqual(fract1.__truediv__(4, 6), "6/5", "fract1.__truediv__(4, 6)")
        self.assertEqual(fract1.__truediv__(-4, 6), "-6/5", "fract1.__truediv__(-4, 6)")

        self.assertRaises(ZeroDivisionError, fract1.__sub__, 2, 0)

    def test_eq(self):
        fract1 = Fraction(4, 5)
        self.assertTrue(fract1.__eq__(4, 5))
        self.assertTrue(fract1.__eq__(-4, -5))

        self.assertFalse(fract1.__eq__(3, 5))
        self.assertFalse(fract1.__eq__(-4, 5))
        self.assertFalse(fract1.__eq__(4, -5))

    def test_float(self):
        fract1 = Fraction(4, 5)
        self.assertEqual(fract1.__float__(), 0.8)
        fract2 = Fraction(-4, 5)
        self.assertEqual(fract2.__float__(), -0.8)

    def test_is_zero(self):
        fract1 = Fraction(0, 5)
        self.assertTrue(fract1.is_zero())

        fract2 =Fraction(4, 5)
        self.assertFalse(fract2.is_zero())

    def test_is_integer(self):
        fract1 = Fraction(10, 5)
        self.assertTrue(fract1.is_integer())

        fract2 = Fraction(4, 5)
        self.assertFalse(fract2.is_integer())

    def test_is_proper(self):
        fract1 = Fraction(4, 5)
        self.assertTrue(fract1.is_proper())

        fract2 = Fraction(5, 5)
        self.assertFalse(fract2.is_proper())

        fract3 = Fraction(7, 5)
        self.assertFalse(fract3.is_proper())

    def test_is_unit(self):
        fract1 = Fraction(5, 10)
        self.assertTrue(fract1.is_unit())

        fract2 = Fraction(12, 10)
        self.assertFalse(fract2.is_unit())
        fract3 = Fraction(-5, 10)
        self.assertFalse(fract3.is_unit())

    def test_adjacent_to(self):
        fract1 = Fraction(4, 5)
        self.assertTrue(fract1.is_adjacent_to(3, 5))

        self.assertFalse(fract1.is_adjacent_to(-3, 5))
        self.assertFalse(fract1.is_adjacent_to(1, 5))

        self.assertRaises(ZeroDivisionError, Fraction, 2, 0)

if __name__ == '__main__':
    unittest.main()