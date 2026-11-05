#1. Escriu un programa que demani l'edat d'una persona (input(), convertit a int) i imprimeixi:

  # "Menor d'edat" si té menys de 18 anys.
  # "Adult" si té entre 18 i 64 anys (ambdós inclosos).
  # "Jubilat" si té 65 anys o més.


edat = int (input("Indica la teva edad: "))

if edat >= 65:
    print("Jubilat")
elif edat >= 18:
    print("Major d'edat")
else:
    print("Menor")


#2. Escriu un programa amb dues variables te_entrada = True i te_reserva = False que imprimeixi "Pot passar" 
# si té entrada o reserva, i "No pot passar" en cas contrari. Fes-ho amb un sol if/else fent servir or.

te_entrada = True
te_reserva = False

if te_entrada or te_reserva:
 print("Pot passar")
else:
   print("No pot passar")

#3. Donada la variable nota = 7.5, escriu un if/elif/else que imprimeixi la qualificació textual:
#"Excel·lent" (≥9), "Notable" (≥7), "Aprovat" (≥5), "Suspès" (<5). Comprova que amb nota = 7.5 s'imprimeix "Notable" 
#i raona per escrit (1 línia) per què no s'arriba a comprovar la condició de "Aprovat".

nota = 7.5

if nota >= 9:
    print("Excel·lent")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprovat")
else:
    print("Suspès")

# No dona aprovat perquè el requisit de Notable es un 7 o més. 

a = 10
b = "10"
print(a == b) #False
print(a == int(b)) #True
print(a != b and a == int(b)) #True