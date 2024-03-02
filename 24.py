# 24.Za Milicu i Anu se čuva koliko puta su obišle teren u 40 minuta. Međutim,
# prilikom unosa podataka desila se zabuna, pa je u varijabli x sačuvana vrijednost
# koja je trebala biti sačuvana u varijabli y i obrnuto. Napisati kod koji mijenja
# mjesta vrijednostima u promjenljivim x i y. Npr. ako je x = 7 i y = 10, poslije
# izvršavanja koda treba da bude x=10 i y=7.

x = int(input("Unesi X: "))
y = int(input("Unesi Y: "))

pom = x
x = y
y = pom

print(x, y)
