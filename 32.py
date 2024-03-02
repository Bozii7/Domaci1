# 32.Dat je šestocifreni broj n (n=abcdef). Provjeriti da li važi a* c + 2 + f = b + d*e.
# Pomoć: razmisliti o provjeri uslova (boolean operator) - samostalno isprobati
# implementaciju iste u Python-u. Ovo ćemo svakako raditi tokom naredne
# sedmice.

broj = input("Unesite sestorocifreni broj: ")
a = int(broj[0])
b = int(broj[1])
c = int(broj[2])
d = int(broj[3])
e = int(broj[4])
f = int(broj[5])

if a * c + 2 + f == b + d * e:
    print(True)
else:
    print(False)
