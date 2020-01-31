from unittest import TestCase

from HenselLifting import HenselLifting
from Polynomial import Polynomial


class HenselLiftingWithNoSolutionTester(TestCase):
    def setUp(self):
        polynomial = Polynomial([-13, -5, 7, 1])
        self.lifting = HenselLifting(polynomial)

    def test_noLift(self):
        self.assertEqual(2, self.lifting.currentDivisor)
        self.assertSetEqual({1}, self.lifting.currentSolutions)

    def test_oneLift(self):
        self.lifting.lift()

        self.assertEqual(4, self.lifting.currentDivisor)
        self.assertSetEqual(set(), self.lifting.currentSolutions)

    def test_twoLifts(self):
        self.lifting.lift()
        self.lifting.lift()

        self.assertEqual(8, self.lifting.currentDivisor)
        self.assertSetEqual(set(), self.lifting.currentSolutions)
