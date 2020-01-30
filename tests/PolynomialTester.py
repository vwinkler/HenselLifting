from unittest import TestCase

from parameterized import parameterized

from Polynomial import Polynomial


class TestPolynomial(TestCase):
    @parameterized.expand([[[], []],
                           [[0], []],
                           [[0, 1], [0, 1]],
                           [[0, 0], [0, 0]],
                           [[1, 0], [1]]])
    def test_init(self, coefficients, trimmedCoefficients):
        self.assertEqual(Polynomial(trimmedCoefficients), Polynomial(coefficients))

    @parameterized.expand([[0, 0],
                           [1, 0]])
    def test_evaluateZeroPolynomial(self, x, result):
        polynomial = Polynomial([])
        self.assertEqual(result, polynomial.evaluate(x))

    @parameterized.expand([[0, 1],
                           [1, -1],
                           [2, 1],
                           [3, 7],
                           [-1, 7]])
    def test_evaluateNonZeroPolynomial(self, x, result):
        polynomial = Polynomial([1, -4, 2])
        self.assertEqual(result, polynomial.evaluate(x))

    @parameterized.expand([[[0], [0]],
                           [[1], [0]],
                           [[0, 1], [1, 0]],
                           [[1, 1], [1, 0]],
                           [[0, 0, 1], [0, 2]]])
    def test_derive(self, coefficients, derivativeCoefficients):
        self.assertEqual(Polynomial(derivativeCoefficients), Polynomial(coefficients).derive())
