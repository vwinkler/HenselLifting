from unittest import TestCase

from HenselLifting import HenselLifting
from Polynomial import Polynomial


class FirstExerciseHenselLiftingTest(TestCase):

    def setUp(self):
        polynomial = Polynomial([-13, -6, 8, 1])
        self.lifting = HenselLifting(polynomial)

    def test_noLift(self):
        self.assertEqual(2, self.lifting.currentDivisor)
        self.assertSetEqual({1}, self.lifting.currentSolutions)

    def test_oneLift(self):
        self.lifting.lift()

        self.assertEqual(4, self.lifting.currentDivisor)
        self.assertSetEqual({3}, self.lifting.currentSolutions)

    def test_twoLifts(self):
        self.lifting.lift()
        self.lifting.lift()

        self.assertEqual(8, self.lifting.currentDivisor)
        self.assertSetEqual({7}, self.lifting.currentSolutions)

    def test_threeLift(self):
        self.lifting.lift()
        self.lifting.lift()
        self.lifting.lift()

        self.assertEqual(16, self.lifting.currentDivisor)
        self.assertSetEqual({15}, self.lifting.currentSolutions)
