'''
19. Napisati program koji za zadati trocifreni broj računa zbir cifara tog broja.
'''

broj = int(input("Unesi trocifreni broj: "))

if broj < 100 and broj > 999:
    print('To nije trocifren broj.')
else:
    j = broj % 10
    d = (broj // 10) % 10
    s = broj // 100
    zbir = j + d + s
    print(zbir)