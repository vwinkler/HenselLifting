from unittest import TestCase

from HenselLifting import HenselLifting
from Polynomial import Polynomial


class SecondExerciseHenselLiftingTester(TestCase):

    def setUp(self):
        polynomial = Polynomial([8, -1, 1])
        self.lifting = HenselLifting(polynomial)

    def test_noLift(self):
        self.assertEqual(2, self.lifting.currentDivisor)
        self.assertSetEqual({0, 1}, self.lifting.currentSolutions)

    def test_oneLift(self):
        self.lifting.lift()

        self.assertEqual(4, self.lifting.currentDivisor)
        self.assertSetEqual({0, 1}, self.lifting.currentSolutions)

    def test_twoLifts(self):
        self.lifting.lift()
        self.lifting.lift()

        self.assertEqual(8, self.lifting.currentDivisor)
        self.assertSetEqual({0, 1}, self.lifting.currentSolutions)

    def test_threeLift(self):
        self.lifting.lift()
        self.lifting.lift()
        self.lifting.lift()

        self.assertEqual(16, self.lifting.currentDivisor)
        self.assertSetEqual({8, 9}, self.lifting.currentSolutions)

    def test_fourLift(self):
        self.lifting.lift()
        self.lifting.lift()
        self.lifting.lift()
        self.lifting.lift()

        self.assertEqual(32, self.lifting.currentDivisor)
        self.assertSetEqual({8, 25}, self.lifting.currentSolutions)
