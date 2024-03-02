#10. Date su koordinate donje desne i gornje lijeve ivice zida (pravougaonik). Izračunati
#povrsinu i obim zida.

x1 = int(input('Unesite vrijednost prve kordinate donje desne ivice: '))
y1 = int(input('Unesite vrijednost druge kordinate donje desne ivice: '))
x2 = int(input('Unesite vrijednost prve kordinate gornje lijeve ivice: '))
y2 = int(input('Unesite vrijednost druge kordinate gornje lijeve ivice: '))

duzina = abs(x1-x2)
visina = abs(y1-y2)

povrsina = duzina * visina

print(povrsina)
