# HenselLifting
Finds all integer solutions of the equation ```p(x) = 0 mod 2^k``` for some ```k > 0``` and some polynomial ```p``` with integer coefficients.

## Input
For ```k = 5``` and ```p(x) = x^3 - 5x^2 + 7x + 13```
put this line into stdin:

    5 1 -5 7 13

## Output
```UNSAT``` if there is no solution or the solutions line by line
