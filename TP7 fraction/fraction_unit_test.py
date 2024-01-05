from fraction import Fraction
import unittest


f_3_5 = Fraction(3, 5)
f_6_5 = Fraction(6, 5)
f_n4_5 = Fraction(-4, 5)
f_0_5 = Fraction(0, 5)
f_0_n5 = Fraction(0, -5)
f_n1_5 = Fraction(-1, 5)
f_4_5 = Fraction(4, 5)
f_2_5 = Fraction(2, 5)
f_4_6 = Fraction(4, 6)
f_n4_6 = Fraction(-4, 6)
f_8_15 = Fraction(8, 15)
f_n1_1 = Fraction(-1, 1)
f_n6_5 = Fraction(-6, 5)
f_n4_n5 = Fraction(-4, -5)
f_4_n5 = Fraction(4, -5)
f_n3_5 = Fraction(-3, 5)
f_1_5 = Fraction(1, 5)
f_5_5 = Fraction(5, 5)
f_7_5 = Fraction(7, 5)
f_10_5 = Fraction(10, 5)
f_5_10 = Fraction(5, 10)
f_12_10 = Fraction(12, 10)
f_n5_10 = Fraction(-5, 10)
f_n3_n5 = Fraction(-3,-5)
f_10_25 = Fraction(10, 25)
f_n9_n15 = Fraction(-9, -15)
f_n80_168 = Fraction(-80, 168)
f_4_1 = Fraction(4, 1)
f_364_17 = Fraction(364, 17)
f_32_3 = Fraction(32, 3)
f_568_4 = Fraction(568, 4)
f_1072_7 = Fraction(1072, 7)
f_2_723 = Fraction(2, 723)
f_n568_4 = Fraction(-568, 4)
f_n2_723 = Fraction(-2, 723)
f_17_455 = Fraction(17, 455)
f_3_160 = Fraction(3, 160)
f_497_536 = Fraction(497, 536)
f_2_1 = Fraction(2, 1)
f_1446_5 = Fraction(1446, 5)
f_5_1446 = Fraction(5, 1446)
f_n10_5 = Fraction(-10, 5)
f_n4_1 = Fraction(-4, 1)
f_n2_1 = Fraction(-2, 1)
f_n1_4 = Fraction(-1, 4)
f_n710_1 = Fraction(-710, 1)


class FractionTestCase(unittest.TestCase):

    def test_init(self):
        self.assertEqual(f_2_5.numerator, 2, "Normal test : numérateur")
        self.assertEqual(f_2_5.denominator, 5, "Normal test : dénominateur")
        self.assertEqual(f_2_5.total, 0.4, "Normal test : representation décimal")
        self.assertEqual(f_2_5.rest, 2, "Normal test : du reste")

        self.assertEqual(f_n3_n5.numerator, 3, "Normal test : numérateur")
        self.assertEqual(f_n3_n5.denominator, 5, "Normal test : dénominateur")
        self.assertEqual(f_n3_n5.total, 0.6, "Normal test : representation décimal")
        self.assertEqual(f_n3_n5.rest, 3, "Normal test : du reste")

        self.assertEqual(f_2_5, f_10_25, "Normal test : simplification de la fraction")
        self.assertEqual(f_n3_n5, f_n9_n15, "Normal test : simplification de la fraction")


        self.assertRaises(ZeroDivisionError, Fraction, 2, 0)

    def test_str(self):
        self.assertEqual(str(f_5_10), "1/2", "Fraction(5, 10)")

        self.assertEqual(str(f_n80_168), "-10/21", "Fraction(-80, 168)")

    def test_as_mixed_number(self):
        fract1 = Fraction(7, 5)
        self.assertEqual(fract1.as_mixed_number(), "1 et 2/5", "Fraction(7,5)")

        fract2 = Fraction(5, 5)
        self.assertEqual(fract2.as_mixed_number(), "1", "Fraction(5,5)")

        fract3 = Fraction(2, 5)
        self.assertEqual(fract3.as_mixed_number(), "2/5", "Fraction(2,5)")

    def test_add(self):
        self.assertEqual(f_3_5 + f_3_5, f_6_5, "fract1.__add__(3, 5)")
        self.assertEqual(f_3_5 + f_n4_5, f_n1_5, "fract1.__add__(-4, 5)")
        self.assertEqual(f_3_5 + f_0_5, f_3_5, "fract1.__add__(0, 5)")

    def test_sub(self):

        self.assertEqual(f_4_5 - f_3_5, f_3_5 - f_2_5, "fract1.__sub__(3, 5)")
        self.assertEqual(f_4_5 - f_n4_5, f_4_5 + f_4_5, "fract1.__sub__(-4, 5)")
        self.assertEqual(f_4_5 - f_0_5, f_4_5, "fract1.__sub__(0, 5)")

    def test_mul(self):

        self.assertEqual(f_4_5 * f_4_6, f_8_15, "fract1.__mul__(4, 6)")
        self.assertEqual(f_4_5 * f_n4_6, f_8_15 * f_n1_1, "fract1.__mul__(-4, 6)")
        self.assertEqual(f_4_5 * f_0_5, f_0_5, "fract1.__mul__(0, 6)")

    def test_truediv(self):
        self.assertEqual(f_4_5 / f_4_6, f_6_5, "(4/5) / (4/6)")
        self.assertEqual(f_4_5 / f_4_5, f_5_5, "(4/5) / (4/5)")
        self.assertEqual(f_4_5 / f_1_5, f_4_1, "(4/5) / (1/5)")
        self.assertEqual(f_4_5 / f_364_17, f_17_455, "(4/5) / (364/17)")
        self.assertEqual(f_1_5 / f_32_3, f_3_160, "(1/5) / (32/3)")
        self.assertEqual(f_568_4 / f_1072_7, f_497_536, "(568/4) / (1072/7)")
        self.assertEqual(f_10_5 / f_5_5, f_2_1, "(10/5) / (5/5)")
        self.assertEqual(f_4_5 / f_2_723, f_1446_5, "(4/5) / (2/723)")
        self.assertEqual(f_2_723 / f_4_5, f_5_1446, "(2/723) / (4/5)")

        self.assertEqual(f_n4_5 / f_4_6, f_6_5 * f_n1_1, "(-4/5) / (4/6)")
        self.assertEqual(f_n4_5 / f_4_5, f_5_5 * f_n1_1, "(-4/5) / (4/5)")
        self.assertEqual(f_n4_5 / f_1_5, f_4_1 * f_n1_1, "(-4/5) / (1/5)")
        self.assertEqual(f_n4_5 / f_364_17, f_17_455 * f_n1_1, "(-4/5) / (364/17)")
        self.assertEqual(f_n1_5 / f_32_3, f_3_160 * f_n1_1, "(-1/5) / (32/3)")
        self.assertEqual(f_n568_4 / f_1072_7, f_497_536 * f_n1_1, "(-568/4) / (1072/7)")
        self.assertEqual(f_n10_5 / f_5_5, f_2_1 * f_n1_1, "(-10/5) / (5/5)")
        self.assertEqual(f_n4_5 / f_2_723, f_1446_5 * f_n1_1, "(-4/5) / (2/723)")
        self.assertEqual(f_n2_723 / f_4_5, f_5_1446 * f_n1_1, "(-2/723) / (4/5)")

        self.assertEqual(f_n4_5 / f_n4_6, f_6_5,"(-4/5) / (-4/6)")
        self.assertEqual(f_1_5 / f_n4_5, f_n1_4,"(1/5) / (-4/5)")
        self.assertEqual(f_568_4 / f_n1_5, f_n710_1,"(568/4) / (-1/5)")
        self.assertEqual(f_10_5 / f_n1_1, f_n2_1,"(10/5) / (-1/1)")


        with self.assertRaises(ZeroDivisionError):
            f_4_5 / f_0_5

        with self.assertRaises(ZeroDivisionError):
            f_4_5 / f_0_n5


    def test_eq(self):

        self.assertTrue(f_4_5 == f_4_5)
        self.assertTrue(f_4_5 == f_n4_n5)

        self.assertFalse(f_4_5 == f_3_5)
        self.assertFalse(f_4_5 == f_n4_5)
        self.assertFalse(f_4_5 == f_4_n5)

    def test_float(self):

        self.assertEqual(float(f_4_5), 0.8)
        self.assertEqual(float(f_n4_5), -0.8)

    def test_is_zero(self):

        self.assertTrue(f_0_5.is_zero())
        self.assertFalse(f_4_5.is_zero())

    def test_is_integer(self):

        self.assertTrue(f_10_5.is_integer())
        self.assertFalse(f_4_5.is_integer())

    def test_is_proper(self):

        self.assertTrue(f_4_5.is_proper())
        self.assertFalse(f_5_5.is_proper())
        self.assertFalse(f_7_5.is_proper())

    def test_is_unit(self):

        self.assertTrue(f_5_10.is_unit())
        self.assertFalse(f_12_10.is_unit())
        self.assertFalse(f_n5_10.is_unit())

    def test_adjacent_to(self):

        self.assertTrue(f_4_5.is_adjacent_to(f_3_5))
        self.assertFalse(f_4_5.is_adjacent_to(f_n3_5))
        self.assertFalse(f_4_5.is_adjacent_to(f_1_5))


if __name__ == '__main__':
    unittest.main()