# Test S5 — Entrada i sortida

Control ràpid d'atenció a classe (RA1, sessió S5)

---

**1.** Què retorna sempre la funció `input()`, sigui quin sigui el que escrigui l'usuari?

    A) Un int
    B) Un float
    C) Un str
    D) Depèn del que escrigui l'usuari

**Resposta:__c__**

**2.** Quin és l'output d'aquest codi si l'usuari escriu `25` quan se li demana?

    edat = input("Edat: ")
    print(edat + 1)

    A) 26
    B) TypeError
    C) 251
    D) "26"

**Resposta:___d_**

**3.** Quin és l'output d'aquest codi?

    nom = "Anna"
    edat = 30
    print(f"{nom} té {edat} anys")

    A) nom té edat anys
    B) {nom} té {edat} anys
    C) Anna té 30 anys
    D) Error, les f-strings no admeten variables

**Resposta:__c__**

**4.** Dins una f-string, es pot posar una expressió (com `edat + 1`) entre claus `{}`?

    A) No, mai
    B) Només si és una variable, no una operació
    C) Només amb la funció eval()
    D) Sí, i s'avalua abans de mostrar el resultat

**Resposta:__d__**

**5.** Quin és l'output d'aquest codi?

    preu = 4.5
    print(f"{preu:.2f}")

    A) 4.5
    B) 4.5000
    C) Error de format
    D) 4.50

**Resposta:__b__**

**6.** Per concatenar un `int` amb un `str` fent servir l'operador `+`, cal:

    A) Convertir l'int a str amb str() primer
    B) No cal fer res, Python ho converteix automàticament
    C) Convertir l'str a int amb int() primer
    D) És impossible en Python

**Resposta:__a__**

**7.** Quin és el resultat d'aquest codi?

    a = input("Primer número: ")
    b = input("Segon número: ")
    print(a + b)

    (l'usuari escriu 3 i 4)

    A) 7
    B) 34
    C) Error
    D) 3 4

**Resposta:__b__**

**8.** Quina lletra s'utilitza abans de les cometes per indicar que una cadena és una f-string?

    A) f
    B) s
    C) r
    D) x

**Resposta:__f__**

**9.** Si es vol que `input()` retorni un número enter directament, cal:

    A) Fer int(input(...))
    B) Fer input(int)
    C) No es pot, sempre cal fer-ho en dos passos
    D) input() ja retorna int automàticament si l'usuari escriu xifres

**Resposta:__c__**

**10.** Quina diferència hi ha entre `print(a, b)` i `print(a + b)` quan `a` i `b` són strings?

    A) Cap, són idèntics
    B) print(a, b) els separa amb un espai automàtic; print(a + b) els concatena sense espai
    C) print(a + b) sempre dona error
    D) print(a, b) dona error si a i b són strings

**Resposta:__b__**
