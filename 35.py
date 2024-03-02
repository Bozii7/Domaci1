# 35.Dat je petocifreni prirodan broj koji predstavlja broj stambene jedinice u zgradi.
# Na osnovu zadatog broja potrebno je odrediti sprat na kome se nalazi stambena
# jedinica. Poznato je da se to može otkriti kada se na vrijednost srednje cifre
# zadatog broja doda vrijednost poslednje cifre. Štampati taj zbir.

br = int(input("Unesi broj: "))
srcif = (br // 100) % 10
poslcif = br % 10
stamb = srcif + poslcif
print(stamb)
