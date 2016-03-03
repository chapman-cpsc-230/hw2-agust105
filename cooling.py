"""
File: cooling.py

Copyright (c) 2016 Francis Agustin

License: MIT

* Query the user for an initial tea temperature `T_tea`, an ambient temperature `T_air` and a number of hours minutes `num_minutes`
* Print a table of the approximate temperature of the tea at each minute $m$ from 0 up to but not including `num_minutes`.`

"""

tea_input = raw_input ("Enter value for T_tea: ")
T_tea = float (tea_input)

air_input = raw_input ("Enter value for T_air: ")
T_air = float (air_input)

min_input = raw_input ("Enter value for minutes: ")
num_minutes = float (min_input)

k = .055

print """
Temperature of air: %d
Number of Minutes: %d

Minute Temperature
""" %(T_air, num_minutes)

i = 0
while i <= num_minutes:
    print "%3.1d    %4.1f" % (i, T_tea)
    T_tea = T_tea - k*(T_tea - T_air)
    i += 1
