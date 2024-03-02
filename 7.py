#7. Marko voli biciklizam. Pošto Marko zna da je važno biti hidratizovan, pije vodu na svakih
#sat vremena vožnje bicikla i to pola litara vode. Kao ulaz poznato je vrijeme u satima, a
#treba štampati broj litara koje će Marko popiti, zaokruženo na najmanju vrijednost (donje
#cijelo).
#Primjer: time = 3 ----> litara = 1; time = 6.7---> litara = 3 ; time = 11.8--> litara = 5
from math import floor
time = float(input("Unesi vrijeme "))
litri = time / 2

print(floor(litri))
