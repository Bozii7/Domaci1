#8. Napisati program kojim se izračunava potrebna dužina trake za ivicu stoljnjaka kružnog
#oblika čija je površina P.
from math import sqrt

PI = 3.14
p = float(input("Unesi povrsinu "))
poluprecnik = sqrt(p / PI)
obim = 2 * poluprecnik * PI
print(obim)
