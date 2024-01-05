import fraction

def test_fraction(num,den):
    try:
        fract = fraction.Fraction(num,den)
        print(fract.__str__)
    except AttributeError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)

test_fraction(0, 4)
test_fraction(3, 0)
test_fraction(3, -5)
test_fraction(-7, 4)
test_fraction(4, 'bbhb')
test_fraction(0, 0)
test_fraction(0, 5)
test_fraction(-45, -234)



