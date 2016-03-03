"""
File: cooling2.py

Copyright (c) 2016 Francis Agustin

License: MIT

EXTRA CREDIT:
* Uses base programming of 'cooling.py'
* Calculates cooling on a second-by-second basis, but still reports the results once for every minute.`

"""

tea_input = raw_input ("Enter value for T_tea: ")
T_tea = float (tea_input)

air_input = raw_input ("Enter value for T_air: ")
T_air = float (air_input)

min_input = raw_input ("Enter value for minutes: ")
num_minutes = float (min_input)

k = .055
k_s = .055/60 # minutes to seconds

print """
Temperature of air: %d
Number of Minutes: %d

Minute Temperature
""" %(T_air, num_minutes)

i = 0 #counts minutes
s = 0 #counts seconds
while i <= num_minutes:

    while s < num_minutes:
        s += 1
        T_tea = T_tea - k_s*(T_tea - T_air)

        print "%3.1d    %4.1f" % (i, T_tea)
        i += 1
