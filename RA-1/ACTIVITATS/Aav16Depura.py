nota1 = 6
nota2 = 7
nota3 = 8
mitjana = (nota1 + nota2 + nota3) / 3
aprova = mitjana >= 5
print(f"Mitjana: {mitjana}, aprova: {aprova}")

# 1. Posa un breakpoint a la línia mitjana = ... i executa amb F5.
# 2. Fes "step over" i mira, al panell "Variables", quin valor pren mitjana (segurament un número molt més gran del que esperaves).
# 3. Identifica quin operador s'està aplicant abans del que tocaria, a causa de la precedència d'operadors. 
# Fes una captura de pantalla!
# 4. Corregeix el codi (amb parèntesis) perquè mitjana sigui realment la mitjana de les tres notes.
# 5. Explica per escrit (2-3 línies) quina regla de precedència provocava el bug.

# En Python, / (i també *, //, %) s’avaluen abans que + i -. Per això nota1 + nota2 + nota3 / 3 només divideix la nota3 entre 3 
# i després suma el resultat. Els parèntesis obliguen a sumar primer les tres notes.
