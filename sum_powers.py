"""
File: sum_power.py

Copyright (c) 2016 Francis Agustin

License: MIT

* Queries the user for a floating point number, which we will call `b` (should not be equal to `1.0`),
 and a natural number, which we will call `n`.
* Computes the sum `1 + b + b^2 + ... + b^n`.
* Prints the result of this computation
* Prints the `b^(n+1)/(b-1)`

"""

user_input = raw_input ("Enter value for b: ")
b = float (user_input)

while b == 1:
    user_input = raw_input ("Value cannot be 1. Enter value for b: ")
    b = float (user_input)

user_input2 = raw_input ("Enter value for n: ")
n = int (user_input2)

i = 0.0
sum_power = 0
while i <= n:
    sum_power += b**i
    i += 1

print sum_power

eq = ((b**(n+1)) - 1)/(b-1)

print eq
