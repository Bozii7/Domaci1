# 26.Dat je četvorocifreni prirodan broj koji predstavlja broj stambene jedinice u
# zgradi. Na osnovu zadatog broja potrebno je odrediti sprat na kome se nalazi
# stambena jedinica. Poznato je da se to može otkriti iz pretposlednje cifre zadatog
# broja.

broj = int(input("Unesi broj: "))
cifra = (broj // 10) % 10
print(cifra)