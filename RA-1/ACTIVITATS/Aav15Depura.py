   a = int(input("Primer número: "))
   b = int(input("Segon número: "))
   suma = a + b
   print(f"La suma és {suma}")    # La suma és 7

# El + no sempre suma: depèn del tipus. input() retorna sempre un str,
# així que a i b són els textos "3" i "4". Entre dos str, el + els
# concatena i dona "34". Per sumar-los cal convertir-los abans amb int().