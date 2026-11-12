nom = "marta"
inicial = nom[0].upper()
print(f"Inicial: {inicial}")

# 1. Posa un breakpoint a la línia de inicial = ....
# 2. Executa el depurador i, amb "step into" o mirant la finestra de variables, comprova quin caràcter conté realment nom[1].
# 3. Identifica per què el resultat no és la inicial correcta (no és un error que Python aturi amb excepció,
# és un error de lògica).
# 4. Corregeix-lo i explica en 2-3 línies quina era la confusió (pista: recorda per quin número comencen els índexs).

# La "m" no es fa majuscula ja que indicaba que l'inicial es "1", lo cual feia que la "a" sigui majuscula.
# Per corregir-ho s'ha de indicar que inicial es el 0, que es la posició correcta de la primera lletra. 