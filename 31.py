# 31.Napisati program koji računa površinu ekrana monitora pravougaonog oblika,
# ukoliko je poznata dužina njegove dijagonale (d = 50) i odnos stranica (aspect
# ratio = 16:9).

from math import sqrt
d = 50

b = d * sqrt(1/4.1604)

a = 16/9*b

print(f'Povrsina ekrana je {round(a*b, 2)} cm kvadratnih')
