from unittest import TestCase

from HenselLifting import HenselLifting
from Polynomial import Polynomial


class HenselLiftingWithNoSolutionTester(TestCase):
    def setUp(self):
        polynomial = Polynomial([13, 7, -5, 1])
        self.lifting = HenselLifting(polynomial)

    def test_noLift(self):
        self.assertEqual(2, self.lifting.currentDivisor)
        self.assertSetEqual({1}, self.lifting.currentSolutions)

    def test_oneLift(self):
        self.lifting.lift()

        self.assertEqual(4, self.lifting.currentDivisor)
        self.assertSetEqual({1, 3}, self.lifting.currentSolutions)

    def test_twoLifts(self):
        self.lifting.lift()
        self.lifting.lift()

        self.assertEqual(8, self.lifting.currentDivisor)
        self.assertSetEqual({1, 3, 5, 7}, self.lifting.currentSolutions)

    def test_threeLifts(self):
        self.lifting.lift()
        self.lifting.lift()
        self.lifting.lift()

        self.assertEqual(16, self.lifting.currentDivisor)
        self.assertSetEqual({1, 3, 5, 7, 9, 11, 13, 15}, self.lifting.currentSolutions)

    def test_fourLifts(self):
        self.lifting.lift()
        self.lifting.lift()
        self.lifting.lift()
        self.lifting.lift()

        self.assertEqual(32, self.lifting.currentDivisor)
        self.assertSetEqual({7, 15, 23, 31}, self.lifting.currentSolutions)
