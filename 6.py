#6. Napisati program koji racuna kvadrat trinoma(a, b, c) koja za unijete parametre a, b i c
#računa kvadrat trinoma za unešene parametre. Formula: 𝑎^2 + 𝑏^2 + 𝑐^2 + 2𝑎𝑏 + 2𝑎𝑐 +
#2𝑏c

a = int(input("Unesi A "))
b = int(input("Unesi B "))
c = int(input("Unesi C "))

kt = pow(a, 2) + pow(b, 2) + pow(c, 2) + 2 * a * b + 2 * a * c + 2 * b * c
print(kt)