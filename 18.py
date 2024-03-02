'''
18. Cijena konzole za igre PlayStation 5 je prvo porasla 10%, pa je smanjena 10%. Ako je
poznata početna cijena konzole, napisati program koji određuje cijenu nakon tih
promjena.
'''

cijena = float(input('Unesi cijenu PS5: '))
cijena = cijena + cijena * 0.1
cijena = cijena - cijena * 0.1
print(cijena)