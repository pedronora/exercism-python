from __future__ import division

class Rational:
    def __init__(self, numer, denom):
        gcd_value = Rational.gcd(numer, denom)
        self.numer = numer / gcd_value
        self.denom = denom / gcd_value

    def gcd(a , b):
        while b:
            a, b = b, a % b
        return a

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)
    
    def __add__(self, other):
        numer = self.numer * other.denom + other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __sub__(self, other):
        numer = self.numer * other.denom - other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = self.denom * other.numer
        return Rational(numer, denom)

    def __abs__(self):
        numer = self.numer if self.numer > 0 else self.numer * -1
        denom = self.denom if self.denom > 0 else self.denom * -1
        return Rational(numer, denom)

    def __pow__(self, power):
        numer = self.numer ** power
        denom = self.denom ** power
        return Rational(numer, denom)
    
    def __rpow__(self, base):
        return base ** (self.numer/self.denom)
