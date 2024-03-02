'''
21. Otkrili ste algoritam kojim možete doći do šifre koja otvara sef. U sefu se nalazi knjiga
koja krije tajne o nastanku univerzuma. Šifra se dobija kada se od kvadrata zbira prve i
poslednje cifre četvorocifrenog broja oduzme razlika kvadrata druge i trece cifre.
'''

broj = int(input("Unesi broj: "))

j = broj % 10
broj //= 10
d = broj % 10
s = (broj // 10) % 10
h = broj // 100

kvadrat_zbira = h ** 2 + 2 * h * j + j ** 2
razlika_kvadrata = (d + s) * (d - s)
sifra = kvadrat_zbira - razlika_kvadrata
print(sifra)
