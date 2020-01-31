import util
from HenselLifting import HenselLifting
from Polynomial import Polynomial

elements = util.readLineOfInts()
k = elements[0]
coefficients = reversed(elements[1:])
lifting = HenselLifting(Polynomial(list(coefficients)))
for i in range(k):
    lifting.lift()
if len(lifting.currentSolutions) == 0:
    print("UNSAT")
for solution in lifting.currentSolutions:
    print(solution)
