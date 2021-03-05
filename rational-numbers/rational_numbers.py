from __future__ import division

def mdc(a, b):
    r = None
    while r != 0:
        r = a % b
        a, b = b, r
    return a

def mmc(a, b):
    return (a * b) / mdc(a, b)

def simplify_fraction(n,d):
    n = int(abs(n))
    d = int(abs(d))
    if n != 0:
        for i in range(max(n, d), 0, -1):
            if d % i == 0 and n % i == 0:
                return i
    return d


class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        self.reduce()

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        den = mmc(self.denom, other.denom)
        num = (den/self.denom*self.numer) + (den/other.denom*other.numer)
        divisor = simplify_fraction(num, den)
        return Rational(num/divisor, den/divisor)

    def __sub__(self, other):
        den = mmc(self.denom, other.denom)
        num = (den/self.denom*self.numer) - (den/other.denom*other.numer)
        divisor = simplify_fraction(num, den)
        return Rational(num/divisor, den/divisor)

    def __mul__(self, other):
        num = self.numer * other.numer
        den = self.denom * other.denom
        divisor = simplify_fraction(num, den)
        return Rational(num/divisor, den/divisor)

    def __truediv__(self, other):
        num = self.numer * other.denom
        den = self.denom * other.numer
        divisor = simplify_fraction(num, den)
        num = num/divisor
        den = den/divisor
        if num < 0 and den < 0:
            num, den = num*-1, den*-1
        if den < 0:
            num, den = num*-1, den*-1
        return Rational(num, den)   

    def __abs__(self):
        num = abs(self.numer)
        den = abs(self.denom)
        return Rational(num, den)

    def __pow__(self, power):
        num = self.numer**power
        den = self.denom**power
        divisor = simplify_fraction(num, den)
        return Rational(num/divisor, den/divisor)

    def __rpow__(self, base):
        return base ** (self.numer/self.denom)

    def reduce(self):
        divisor = simplify_fraction(self.numer, self.denom)
        num = self.numer/divisor
        den = self.denom/divisor
        if num < 0 and den < 0:
            num, den = num*-1, den*-1
        if den < 0:
            num, den = num*-1, den*-1
        self.numer = num
        self.denom = den
