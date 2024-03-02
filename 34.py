# 34.Dobili ste zadatak da generišete specijalni identifikacioni broj za pristup tajnom
# laboratorijskom sektoru. Otkrili ste da se identifikacioni broj može dobiti na
# osnovu poznatog šestocifrenog broja tako što se kvadrira suma cifara tog broja,
# a zatim od tog rezultata oduzme proizvod treće i četvrte cifre istog broja. Kao
# rezultat prikazati identifikacioni broj.

broj = int(input("Unesi broj: "))
pr = broj
sum = 0
while pr != 0:
    cif = pr % 10
    sum += cif
    pr //= 10
sum = pow(sum, 2)

cif3 = (broj // 1000) % 10
cif4 = (broj // 100) % 10

id = sum - (cif3 * cif4)
print(id)



