# 27.Dat je četvorocifreni prirodan broj. Napisati kod koji štampa kvadrat zbira cifara
# tog broja.

broj = int(input("Unesi broj: "))
j = broj % 10
broj //= 10
d = broj % 10
s = (broj // 10) % 10
h = broj // 100
zbir = j + d + s + h
print(zbir ** 2)
