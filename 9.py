#9. Fudbalski teren dimenzija d×s treba ograditi pravougaonom ogradom tako da je
#rastojanje stranica ograde od linije terena r. Napiši program koji određuje dužinu ograde.
#Ulaz: U tri reda standardnog ulaza nalaze se tri cijela broja:
#• d - dužina terena u metrima
#• s - širina terena u metrima
#• r - rastojanje ograde od terena u metrima
#Izlaz: Duzina ograde u metrima

d = int(input("Unesi duzinu "))
s = int(input("Unesi sirinu "))
r = int(input("Unesi rastojanje "))

d = d + 2 * r
s = s + 2 * r

o = 2 * (d + s)
print(o)