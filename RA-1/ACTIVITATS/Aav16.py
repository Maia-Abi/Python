# 1. Calcula i mostra el resultat de 17 // 5, 17 % 5 i 17 / 5. Explica la diferència entre els tres.

print (17 // 5) #3      És la divisió entera.
print (17 % 5)  #2      És el residu de la divisió.
print (17 / 5)  #3.4    És la divisió normal i retorna un float.

# 2. Calcula -17 // 5 i -17 % 5. Compara amb l'exercici anterior: què canvia amb un operand negatiu?

print (-17 // 5) #-4
print (-17 % 5)  #3

# // arrodoneix cap a menys infinit (−3.4 → −4), no cap a zero. I % compleix −17 = 5·(−4) + 3, així que el residu és 3, positiu.

# 3. Declara a = 5, b = 10, c = 15 i, usant els operadors de comparació, 
# calcula en una sola expressió booleana si a < b and b < c. Mostra el resultat i el seu tipus.

a = 5
b = 10
c = 15

resultat = a < b and b < c
print(resultat, type(resultat))   # True <class 'bool'>

# 4. Calcula el resultat de 2 + 3 * 4 ** 2 sense usar parèntesis, i després reescriu la mateixa expressió 
# (mateixos números i operadors: 2, +, 3, *, 4, **, 2) afegint-hi parèntesis perquè el resultat sigui 80.

print(2 + 3 * 4 ** 2)     
print((2 + 3) * 4 ** 2)   

# 5. Prova 5 > 3 and 2 > 4 or 1 == 1 i explica per escrit, pas a pas, com s'avalua (precedència: and abans que or).

print(5 > 3 and 2 > 4 or 1 == 1)   # True

# Es avaluen les comparacions: True and False or True.
# and té més precedència que or: (True and False) → False.
# Queda False or True → True.
