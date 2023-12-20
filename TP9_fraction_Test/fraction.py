def pgcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


class Fraction:
    """Classe représentant une fraction et opérations sur celle-ci

    Auteur : J.Verkyndt
    Date : Decembre 2022
    Cette classe permet des manipulations de fractions via plusieurs opérations.
    """

    def __init__(self, num, den):
        """Cela construit une fraction basée sur un numérateur et un dénominateur.

                PRE : -le numerateur et le dénominateur doiventt etre des entier
                -le dénominateur doit etre différent de 0.
                POST :/
                RAISES : -ZeroDivisionError si dénominateur = 0
        """
        if den == 0:
            raise ZeroDivisionError("Le denominateur ne peut pas être zero.")
        else:
            div = pgcd(num, den)
            self.num = int(num/div)
            self.den = int(den/div)
            self.total = self.num / self.den
            self.rest = self.num % self.den

    @property
    def numerator(self):
        return self.num

    @property
    def denominator(self):
        return self.den

    # ------------------ Textual representations ------------------

    @property
    def __str__(self):
        """
                Renvoie une représentation textuelle de la forme réduite de la fraction

                PRE : /
                POST : Renvoie une fraction num/den réduite

        """
        return str(self.num) + "/" + str(self.den)

    def as_mixed_number(self):
        """
                Renvoie une représentation textuelle de la forme réduite de la fraction sous la forme d'un nombre fractionnaire
                Un nombre fractionnaire est la somme d'un entier et d'une fraction propre

                PRE :/
                POST :Retourne soit un entier, une fraction ou un entier plus une fraction
        """
        if self.total > 1 and self.rest != 0:
            div = pgcd(self.rest, self.den)
            return str(int(self.num // self.den)) + " et " + str(int(self.rest / div)) + "/" + str(int(self.den / div))
        elif self.rest == 0:
            return str(int(self.num/self.den))
        else:
            return str(int(self.num)) + "/" + str(int(self.den))

    # ------------------ Operators overloading ------------------

    def __add__(self, numbis, denbis):
        """
                Surcharge de l'opérateur + pour les fractions

                 PRE :-Le terme a aditionner doit etre une fraction avec un entier comme numérateur et dénominateur
                 POST : -Renvoie une fraction num/den réduite
                 RAISES : -ZeroDivisionError si dénominateur = 0
        """
        if denbis == 0:
            raise ZeroDivisionError("Le denominateur ne peut pas être zero.")
        else:
            num = (self.num * denbis) + (numbis * self.den)
            den = (denbis * self.den)
            div = pgcd(num, den)
            return str(int(num/div)) + '/' + str(int(den/div))

    def __sub__(self, numbis, denbis):
        """
                Surcharge de l'opérateur - pour les fractions

                PRE :-Le terme a soustraire doit etre une fraction avec un entier comme numérateur et dénominateur
                POST : -Renvoie une fraction num/den réduite
                RAISES : -ZeroDivisionError si dénominateur = 0
        """
        if denbis == 0:
            raise ZeroDivisionError("Le denominateur ne peut pas être zero.")
        else:
            num = (self.num * denbis) - (numbis * self.den)
            den = (denbis * self.den)
            div = pgcd(num, den)
            return str(int(num / div)) + '/' + str(int(den / div))

    def __mul__(self, numbis, denbis):
        """
                Surcharge de l'opérateur * pour les fractions

                PRE :-La fraction utiliser pour la multiplication doit avoir un entier comme numerateur et dénominateur
                POST : -Renvoie une fraction num/den réduite
                RAISES : -ZeroDivisionError si dénominateur = 0
        """
        if denbis == 0:
            raise ZeroDivisionError("Le denominateur ne peut pas être zero.")
        else:
            num = (self.num * numbis)
            den = (self.den * denbis)
            div = pgcd(num, den)
            return str(int(num / div)) + '/' + str(int(den / div))

    def __truediv__(self, numbis, denbis):
        """
                Surcharge de l'opérateur / pour les fractions

                PRE : -La fraction utiliser pour la division doit avoir un entier comme numerateur et dénominateur
                -La fraction utiliser pour la division ne doit pas valoir zéro donc le numbis ne peut pas être 0
                POST : -Renvoie une fraction num/den réduite
                RAISES : -ZeroDivisionError si dénominateur = 0
        """
        if denbis == 0:
            raise ZeroDivisionError("Le denominateur ne peut pas être zero.")
        else:
            num = (self.num * denbis)
            den = (self.den * numbis)
            div = pgcd(num, den)
            return str(int(num / div)) + '/' + str(int(den / div))

    def __pow__(self, other):
        """
                Surcharge de l'opérateur ** pour les fractions
                PRE : -Le terme exposant doit etre un nombre entier.
                POST : -Renvoie une fraction num/den réduite
        """
        numexpo = self.num ** other
        denexpo = self.den ** other
        div = pgcd(numexpo, denexpo)
        return str(int(numexpo / div)) + "/" + str(int(denexpo / div))

    def __eq__(self, numbis, denbis):
        """
            Surcharge de l'opérateur == pour les fractions
                PRE : La fraction utiliser pour la l'égalité doit avoir un entier comme numerateur et dénominateur
                POST : Renvoi 'True' si les fractions son égale sinon renvoi 'False'
                RAISES : -ZeroDivisionError si dénominateur = 0
        """
        if denbis == 0:
            raise ZeroDivisionError("Le denominateur ne peut pas être zero.")
        else:
            numa = (self.den * numbis)
            numb = (denbis * self.num)
            return numa == numb

    def __float__(self):
        """Renvoie la valeur décimale de la fraction

                PRE : /
                POST :-La valeur de retour doit étre un nombre décimal.
        """
        return self.num / self.den

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """
            Vérifier si la valeur d'une fraction est 0

                PRE : /
                POST : Renvoi 'True' si la fraction est égale à zero, sinon renvoi 'False'
        """
        return self.total == 0

    def is_integer(self):
        """
            Vérifier si une fraction est un entier (ex : 8/4, 3, 2/2, ...)

                PRE : /
                POST : Renvoi 'True' si la fraction est un entier, sinon renvoi 'False'
        """
        return self.num % self.den == 0

    def is_proper(self):
        """
            Vérifiez si la valeur absolue de la fraction est < 1

                PRE : /
                POST : Renvoi 'True' si la fraction est < 1, sinon renvoi 'False'
        """
        return self.total < 1

    def is_unit(self):
        """
            Vérifier si le numérateur d'une fraction est 1 sous sa forme réduite

                PRE :/
                POST : Renvoi 'True' si le numérateur est 1, sinon renvoi 'False'
        """
        div = pgcd(self.num, self.den)
        return self.num / div == 1

    def is_adjacent_to(self, numbis, denbis):
        """
                Vérifier si deux fractions diffèrent d'une fraction unitaire

                Deux fractions sont adjacentes si la valeur absolue de leur différence est une fraction unitaire

                PRE : La fraction utiliser doit avoir un entier comme numerateur et dénominateur
                POST : Renvoi 'True' si les deux fraction diffèrent d'une fraction unitaire, sinon renvoi 'False'
                RAISES : -ZeroDivisionError si dénominateur = 0
        """
        if denbis == 0:
            raise ZeroDivisionError("Le denominateur ne peut pas être zero.")
        else:
            num = (self.num * denbis) - (numbis * self.den)
            den = (denbis * self.den)
            div = pgcd(num, den)
            return (num / div) == 1 or (num / div) == -1
