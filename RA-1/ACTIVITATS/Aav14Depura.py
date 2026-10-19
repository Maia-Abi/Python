   preu = float("20")   # o preu = 20.0    
   iva = 0.21
   total = preu + (preu * iva)
   print(f"Total: {total}")   # Total: 24.2

   # El codi fallava perquè preu = "20" és un text (str), no un número,
   # encara que sembli un número. Python només pot multiplicar un text per
   # un enter (per repetir-lo), no per un float com 0.21, i per això dona TypeError.
   # Cal convertir preu a float abans de fer càlculs.