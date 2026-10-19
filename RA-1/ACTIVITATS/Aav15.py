nom = input("Com et dius? ")
edat = input("Quants anys tens? ")
print(f"{nom} té {edat} anys")

a = int(input("Primer número: "))
b = int(input("Segon número: "))
print(f"La suma és {a + b}")

print(f"D'aquí a 10 anys tindràs {int(edat) + 10} anys")

preu = 12.5
print(f"El preu és {preu:.2f} €")    # El preu és 12.50 €

# El + no sempre suma: depèn del tipus. input() retorna sempre un str,
# així que a i b són els textos "3" i "4". Entre dos str, el + els
# concatena i dona "34". Per sumar-los cal convertir-los abans amb int().