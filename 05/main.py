#!/usr/bin/env python3

# Ötödik gyakorlati óra kódjai

# Az enumerate a range-hez hasonlóan egy iterátor.
# Tuple-öket ad vissza.

# Pass kulcsszó: üres utasítás, kb olyan, mint egy # TODO.

# Docstring függvényekbe megy be. Az adott függvény docstringjét le tudjuk kérdezni.
    # függvény.__doc__
# Ez a docstring benne lesz az adott fügvény help-jében

# Opcionális paramétereket adhatunk meg a függvényeinknek.
# Ezeknek a paramétereknek a nevét nem kötelező feltüntetni híváskor, de akkor fontos a sorrend.
# Kötelező paraméternél is adhatunk értéket, annak ellenére, hogy nem kötelező. (Certiporton előfordulhat))

# Halmaz adatszerkezet
# Minden eleme egyedi.
# Elemeknek nincsen fix sorrendje.
# set()
# Halmazműveletek elérhetőek.
# A halmaz hash függvényt alkalmaz, ezért lesz tetszőleges a sorrend.



def greet(name, greetings="Hello"):
    print(f"{greetings} {name}!")


def hello(name, repeat=1, postfix=""):
    for i in range(repeat):
        print(name + postfix)


def debugger(szamok, debug=False):
    if debug:
        print("# ciklus kezdete")
        for szam in szamok:
            print(szam, end=", ")
        print("\n# ciklus vége")
    else:
        for szam in szamok:
            print(szam)


def main():
    li = ["alfa", "beta", "gamma"]

    # két változós for ciklus: kicsomagoljuk a tuple-t
    # a start egy opcionális paraméter, az értéktől indul az indexelés
    for idx, e in enumerate(li, start = 1):
        print(idx, e)
    

    greet("Richard")
    greet("Richard", greetings="Hola")
    greet("Richard", greetings="Bonjour")

    hello("Richard")
    print("---")
    hello("Richard", repeat=3)
    print("---")
    hello("Richard", repeat=2, postfix="!")

    debugger([1, 2, 3, 4, 5])
    debugger([1, 2, 3, 4, 5], debug=True)

if __name__ == "__main__":
    main()