7 / 2    # 3.5
7 // 2   # 3
7 % 2    # 1
2 ** 3   # 8

x = 7
print(1 < x < 10)          # True   (equival a: 1 < x and x < 10)
print(1 < x and x < 5)     # False  (x val 7, no és menor que 5)

print(-7 // 2)   # -4  (no -3)
print(-7 % 2)    # 1   (el residu té el mateix signe que el divisor, 2)
print(7 // -2)   # -4
print(7 % -2)    # -1

x = 5
if x = 5:
    print("mal")
# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?