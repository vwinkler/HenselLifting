from lib2to3.fixes.fix_import import traverse_imports


class Polynomial:
    def __init__(self, coefficients):
        trailingZeros = countTrailingZeros(coefficients)
        self.coefficients = coefficients if trailingZeros == 0 else coefficients[:-trailingZeros]

    def evaluate(self, x):
        result = 0
        for (i, coefficient) in enumerate(self.coefficients):
            result += coefficient * x ** i
        return result

    def derive(self):
        derivativeCoefficients = [self.coefficients[i + 1] * (i + 1) for i in range(len(self.coefficients) - 1)]
        return Polynomial(derivativeCoefficients)

    def __eq__(self, object):
        if not isinstance(object, Polynomial):
            return False

        return object.coefficients == self.coefficients

    def __repr__(self):
        if len(self.coefficients) > 0:
            stringRepresentation = ""
            for i in reversed(range(1, len(self.coefficients))):
                stringRepresentation += "{}x^{} + ".format(self.coefficients[i], i)
            return "{}{}".format(stringRepresentation, self.coefficients[0])
        else:
            return "0"


def countTrailingZeros(coefficients):
    zeroCount = 0
    for c in coefficients:
        if c == 0:
            zeroCount += 1
        else:
            zeroCount = 0
    return zeroCount
