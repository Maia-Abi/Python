def mitjana(notes):
    suma = 0
    for n in notes:
        suma += n          # <- posem un breakpoint aquí
    return suma / len(notes)

resultat = mitjana([6, 7, 5, 9])
print(resultat)
