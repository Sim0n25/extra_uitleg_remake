#!/usr/bin/env python
"""info over project"""

#import

...

__author__ = "Simon Fransen"
__email__ = "simon.fransen@student.kdg.be"
__status__ = "Production"


getallen = [1, 2, 3, 4, 5, 6]
som_getallen = 0
for getal in getallen:
    if som_getallen < 10:
        som_getallen+=getal
    else:
        break
    print(getal)
print('Som van de getallen:', som_getallen)