class HenselLifting:
    def __init__(self, polynomial):
        self.polynomial = polynomial
        self.derivative = polynomial.derive()
        self.currentSolutions = set()
        self.setInitialSolutions()

    def lift(self):
        previousSolutions = self.currentSolutions
        self.currentSolutions = set()
        for x in previousSolutions:
            self.liftForPreviousSolution(x)
        self.currentDivisor *= 2

    def liftForPreviousSolution(self, x):
        if self.derivative.evaluate(x) % 2 == 0:
            self.addZeroOrTwoLiftedSolutions(x)
        else:
            self.doUniqueLifting(x)

    def doUniqueLifting(self, x):
        self.currentSolutions.add((x - self.polynomial.evaluate(x)) % (2 * self.currentDivisor))

    def addZeroOrTwoLiftedSolutions(self, x):
        if self.polynomial.evaluate(x) % (2 * self.currentDivisor) == 0:
            self.currentSolutions.add(x)
            self.currentSolutions.add(x + self.currentDivisor)

    def setInitialSolutions(self):
        for i in [0, 1]:
            if self.polynomial.evaluate(i) % 2 == 0:
                self.currentSolutions.add(i)
        self.currentDivisor = 2
