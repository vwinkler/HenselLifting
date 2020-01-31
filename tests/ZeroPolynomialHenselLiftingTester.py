from unittest import TestCase

from HenselLifting import HenselLifting
from Polynomial import Polynomial


class FirstExerciseHenselLiftingTest(TestCase):

    def setUp(self):
        polynomial = Polynomial([])
        self.lifting = HenselLifting(polynomial)

    def test_noLift(self):
        self.assertEqual(2, self.lifting.currentDivisor)
        self.assertSetEqual({0, 1}, self.lifting.currentSolutions)

    def test_oneLift(self):
        self.lifting.lift()

        self.assertEqual(4, self.lifting.currentDivisor)
        self.assertSetEqual({0, 1, 2, 3}, self.lifting.currentSolutions)
