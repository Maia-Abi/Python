# 1. Escriu un condicional niuat que, donat un número enter x, imprimeixi:

    # "Positiu i parell" si és positiu i parell.
    # "Positiu i senar" si és positiu i senar.
    # "Zero" si és 0.
    # "Negatiu" si és negatiu. Prova-ho amb x = 8, x = 7, x = 0 i x = -3.

x = -4

if x >= 0:
    if x % 2 == 0:
        print("Major que 10 i parell")
    else:
        print("Major que 10 i senar")

if x == 0:
        print("Zero")

if x < 0:
        print("Negatiu")


# 2. Reescriu l'apartat 1 (només el cas "positiu") sense niuar, utilitzant and en una sola condició if. 
# Comprova que dona el mateix resultat.

x = 18

if x >= 0 and x % 2 == 0:
        print("Major que 10 i parell")
elif x > 0 and x % 2 != 0:
        print("Major que 10 i senar")


# 3. Donat paraula = "programacio":

    # Imprimeix el primer i l'últim caràcter (amb índex negatiu).
    # Imprimeix els 4 primers caràcters amb slicing.
    # Imprimeix la paraula al revés amb slicing ([::-1]).
    # Imprimeix els caràcters de dos en dos (paraula[::2]).

Paraula = "Programació"

print (Paraula[0],Paraula[-1], sep="")
print (Paraula[0:4])
print (Paraula[::-1])
print (Paraula[::2])
