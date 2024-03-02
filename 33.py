# 33.Napisati program koji provjerava koliko se poligona kvadratnog oblika i zadatih
# dimenzija može kreirati na jednoj poljani za koju su poznate njena širina i dužina.

p1 = 514 * 130

a = int(input("Unesi duzinu stranice: "))
p2 = a * a
rezultat = p1 // p2

print(rezultat)