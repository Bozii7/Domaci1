'''
20. Dobili ste zadatak da dešifrujete kod kojim se otvaraju tajna vrata. Otkrili ste da na
osnovu poznatog trocifrenog broja možete pronaći kod koji otvara tajna vrata tako što od
proizvoda cifara tog broja oduzmete zbir cifara istog broja.
'''

broj = int(input('Unesi trocifreni broj'))

j = broj % 10
d = (broj // 10) % 10
s = broj // 100

proiz = j * d * s
sum = j + d + s

sifra = proiz - sum
print(sifra)