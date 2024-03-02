#28.Dat je trocifren broj. Odrediti broj koji se dobija zamjenom prve i posljednje cifre.

broj = int(input("Unesi broj: "))
j = broj % 10
d = (broj // 10) % 10
s = broj // 100

broj = 100 * j + 10 * d + s
print(broj)