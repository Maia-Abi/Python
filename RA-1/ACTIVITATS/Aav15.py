nom = input("Com et dius? ")
edat = input("Quants anys tens? ")
print(f"{nom} té {edat} anys")

a = int(input("Primer número: "))
b = int(input("Segon número: "))
print(f"La suma és {a + b}")

print(f"D'aquí a 10 anys tindràs {int(edat) + 10} anys")

preu = 12.5
print(f"El preu és {preu:.2f} €")    # El preu és 12.50 €

# Amb + només puc unir textos: si hi ha un número l'he de convertir amb str()
# i he de posar els espais a mà, cosa que fa el codi més llarg i fàcil d'embolicar.
# Amb una f-string escric les variables dins de {} i Python les converteix sol.
# És més llegible i permet fer càlculs i formatar (per exemple :.2f) dins les claus.