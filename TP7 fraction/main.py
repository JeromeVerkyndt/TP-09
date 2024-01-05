import fraction


def test_fraction(num, den):
    try:
        fract = fraction.Fraction(num, den)
        print (str(fract))
    except AttributeError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)


test_fraction(1, -2)
test_fraction(3, 0)
test_fraction(3, -5)
test_fraction(-7, 4)
test_fraction(-45, -234)

print("---------------------------")
test_deux = fraction.Fraction(7, 5)
fract_bis = fraction.Fraction(3, 4)
print(test_deux.as_mixed_number())
print(str(test_deux))
print(str(test_deux - fract_bis))
print(str(test_deux*fract_bis))
print(str(test_deux/fract_bis))
print(str(test_deux ** 3))
print(test_deux==fract_bis)
print(float(test_deux))
print(test_deux.is_zero())
print(test_deux.is_integer())
print(test_deux.is_proper())
print(test_deux.is_unit())
print(test_deux.is_adjacent_to(fract_bis))
