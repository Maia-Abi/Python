numero = 10          # int
decimal = 3.14       # float
text = "Hola"        # str
veritat = True       # bool

print(numero, type(numero))
print(decimal, type(decimal))
print(text, type(text))
print(veritat, type(veritat))

preu_text = "12.50"
preu_amb_iva = float(preu_text) * 1.21   # 15.125
print(preu_amb_iva, type(preu_amb_iva))

edat = 17
es_major = edat >= 18     # False
print(es_major, type(es_major))

print(bool(0))  #False, El zero és fals
print(bool(1))  #True, Qualsevol número diferent de 0 és cert
print(bool(""))  #False, Cadena buida = fals
print(bool("False"))  #True, És una cadena amb contingut; Python no n’interpreta el significat
print(bool("0"))  #True, Igual: és un text no buit, no el número 0

"5" + 5 #Python no barreja text amb números, llavors dona error. Per això cal convertir el número a text o el text a número.