x = 15
if x > 10:
    if x % 2 == 0:
        print("Major que 10 i parell")
    else:
        print("Major que 10 i senar")
# Output: Major que 10 i senar

paraula = "Python"
print(paraula[0])    # P
print(paraula[-1])   # n
print(paraula[10])   # IndexError

paraula = "Python"
print(paraula[0:3])   # Pyt
print(paraula[2:])    # thon
print(paraula[:2])    # Py
print(paraula[::-1])  # nohtyP
print(paraula[0:100]) # Python (no dona error)