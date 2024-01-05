def pgcd(a,b) :
   while a%b != 0 :
      a, b = b, a%b
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
                -AttributeError si
        """
        if ((type(num) is float ) or (type(num) is int)) and ((type(den) is int) or (type(den) is int)):
            if den == 0:
                raise ZeroDivisionError("Le denominateur ne peut pas être zero.")
            else:
                self.num = num
                self.den = den
                self.total = self.num / self.den
                self.rest = self.num % self.den
        else:
            raise AttributeError("Le numerateur et le denominateur doit être un nombre reel pas une chaine de caractere ou autres.")

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

                PRE : (- les termes doivent être des nombres réel donc pas des chaines de caracteres)
                POST :-La fraction doit être simplifier le plus possible donc ne dois pas avoir de numérateur ou dénominateur a virgule.

        """
        if self.den == 0:
            raise ZeroDivisionError("Le dénominateur d'une fraction ne peut pas être zéro.")
        else:
            div = pgcd(self.num, self.den)
            return str(int(self.num / div)) + "/" + str(int(self.den / div))

    def as_mixed_number(self):
        """
                Renvoie une représentation textuelle de la forme réduite de la fraction sous la forme d'un nombre fractionnaire
                Un nombre fractionnaire est la somme d'un entier et d'une fraction propre

                PRE :-La fraction doit valoir plus que 1.
                POST :-La reponse doit etre un entier plus une fraction qui ne vaut pas zéro.
        """
        if self.total > 1 and self.rest != 0:
            div = pgcd(self.rest, self.den)
            return str(int(self.num // self.den)) + " et " + str(int(self.rest / div)) + "/" + str(int(self.den / div))
        else:
            raise ValueError("Cette fraction ne peut pas être représenter par un entier et une fracrtion")

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """
                Surcharge de l'opérateur + pour les fractions

                 PRE :-Le terme a aditionner doit etre un nombre réel et pas une chaine de caractere.
                 POST : -La fraction etre la plus simplifie possible.
        """
        if (type(other) is float) or (type(other) is int):
            somme = self.num + (other * self.den)
            div = pgcd(somme, self.den)
            return str(int(somme/div)) + "/" + str(int(self.den/div))
        else:
            raise AttributeError("Le terme a additionner n'est pas un nombre réel")

    def __sub__(self, other):
        """
                Surcharge de l'opérateur - pour les fractions

                PRE :-Le terme a soustraire doit etre un nombre réel et pas une chaine de caractere.
                POST : -La fraction etre la plus simplifie possible.
        """
        if (type(other) is float) or (type(other) is int):
            difference = self.num - (other * self.den)
            div = pgcd(difference, self.den)
            return str(int(difference / div)) + "/" + str(int(self.den / div))
        else:
            raise AttributeError("Le terme à soustraire n'est pas un nombre réel")

    def __mul__(self, other):
        """
                Surcharge de l'opérateur * pour les fractions

                PRE :-Le terme multiplicateur doit etre un nombre réel et pas une chaine de caractere.
                POST : -La fraction etre la plus simplifie possible.
        """
        if (type(other) is float) or (type(other) is int):
            quotient = self.num * other
            div = pgcd(quotient, self.den)
            return str(int(quotient / div)) + "/" + str(int(self.den / div))
        else:
            raise AttributeError("Le terme multiplicateur n'est pas un nombre réel")

    def __truediv__(self, other):
        """
                Surcharge de l'opérateur / pour les fractions

                PRE : -Le terme diviseur ne doit pas être zéro.
                -Le terme diviseur doit etre un nombre réel et pas une chaine de caractere.
                POST : -La fraction etre la plus simplifie possible.
        """
        if (type(other) is float) or (type(other) is int):
            if other == 0:
                raise ZeroDivisionError("Le terme diviseur ne peut pas être zéro")
            else:
                dividende = self.den * other
                div = pgcd(self.num, dividende)
                return str(int(self.num / div)) + "/" + str(int(dividende / div))
        else:
            raise AttributeError("Le terme diviseur n'est pas un nombre réel")

    def __pow__(self, other):
        """
                Surcharge de l'opérateur ** pour les fractions
                PRE : -Le terme exposant doit etre un nombre réel et pas une chaine de caractere.
                POST : -La fraction etre la plus simplifie possible.
        """
        if (type(other) is float) or (type(other) is int):
            numexpo = self.num ** other
            denexpo = self.den ** other
            div = pgcd(numexpo, denexpo)
            return str(int(numexpo / div)) + "/" + str(int(denexpo / div))
        else:
            raise AttributeError("Le terme à mettre en exposant n'est pas un nombre réel.")

    def __eq__(self, other):
        """
            Surcharge de l'opérateur == pour les fractions
                PRE : -Le terme entré doit etre un nombre reel et pas une chaine de caractere.
                POST : /
        """
        if (type(other) is float) or (type(other) is int):
            if self.total == other:
                return str(int(self.num)) + "/" + str(int(self.den)) + " et " + str(int(other)) + " sont égaux."
            else:
                return str(int(self.num)) + "/" + str(int(self.den)) + " et " + str(int(other)) + " ne sont pas égaux."
        else:
            raise AttributeError("Le terme entrée n'est pas un nombre réel.")

    def __float__(self):
        """Renvoie la valeur décimale de la fraction

                PRE : /
                POST :-La valeur de retour doit étre un nombre décimal.
        """
        return (self.num / self.den)



    # ------------------ Properties checking ------------------

    def is_zero(self):
        """
            Vérifier si la valeur d'une fraction est 0

                PRE : /
                POST : -La fraction doit valoir zero
        """
        if self.total == 0:
            return "La Fraction est égal à zero"
        else:
            return "La Fraction n'est pas égal à zero"

    def is_integer(self):
        """
            Vérifier si une fraction est un entier (ex : 8/4, 3, 2/2, ...)

                PRE : /
                POST : -La fraction doit etre un entier
        """
        if self.num % self.den == 0:
            return True
        else:
            return False

        return self.num % self.den ==0

    def is_proper(self):
        """
            Vérifiez si la valeur absolue de la fraction est < 1

                PRE : /
                POST : -La valeur absolue de la fraction doit être moins que 1.
        """
        if self.total < 1:
            return "La valeur absolue est plus petite que 1"
        else:
            return "La valeur absolue n'est pas plus petite que 1"

    def is_unit(self):
        """
            Vérifier si le numérateur d'une fraction est 1 sous sa forme réduite

                PRE : -La fraction doit etre le plus réduit possible.
                POST : -Le numérateur de la fraction doit être 1.
        """
        div = pgcd(self.num, self.den)
        if self.num / div == 1:
            return "Le numérateur de la fraction sous sa forme réduite est 1"
        else:
            return "Le numérateur de la fraction sous sa forme réduite n'est pas 1"

    def is_adjacent_to(self, numbis, denbis):
        """
                Vérifier si deux fractions diffèrent d'une fraction unitaire

                Deux fractions sont adjacentes si la valeur absolue de leur différence est une fraction unitaire

                PRE : -Les termes entrer doivent être des nombre reel et pas des chaines de caracteres.
                -les deux fraction doivent être mise sur un dénominateur commun.
                POST : -Les fraction doivent différer d'une fraction unitaire.
        """
        if ((type(numbis) is float ) or (type(numbis) is int)) and ((type(denbis) is int) or (type(denbis) is int)):
            numdiff = (self.num * denbis) - (numbis * self.den)
            dendiff = self.den * denbis
            div = pgcd(numdiff, dendiff)
            if (numdiff / div == 1) or (numdiff / div == -1):
                return "Les deux fraction diffèrent l'une de l'autre d'une fraction unitaire"
            else:
                return "Les deux fraction ne diffèrent pas l'une de l'autre d'une fraction unitaire"
        else:
            raise AttributeError("Les terme entrée ne son pas des nombres reel.")