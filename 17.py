'''
17. Knjižara "Bukvarnica" je posebno mjesto gdje svaka knjiga ima svoju priču. Kako bi
proslavili dolazak novog godišnjeg doba, knjižara je odlučila da uvede popust - svaka
knjiga dobija popust koji se može otkriti samo uz pomoć programa. Kao pomoćnik u
knjižari, vaš zadatak je da kreirate program koji će izračunati konačnu cijenu knjige
nakon primijenjenog popusta.
'''

cijena = float(input("Unesi cijenu knjige: "))
popust = int(input("Unesi popust: "))

cijena = cijena - cijena * (popust / 100)
print(cijena)