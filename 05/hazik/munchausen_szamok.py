#!/usr/bin/env python3


"""
Münchhausen-számok kiszámítása

Egy természetes számot akkor nevezünk Münchausen-számnak, 
ha minden egyes számjegyét az adott számjegy által meghatározott hatványra emelve, 
majd ezen hatványok összegét véve az eredeti számot kapjuk vissza.

Ennél a feladatnál a 0^0 = 0 szabályt alkalmazzuk
"""

# 1. feladat
def munchausen_v1():
    """
    Ennél a függvénynél egy kisebb intervallumon dolgozunk.
    Megnézzük, hogy melyik 10000 alatti számok Münchhausen-számok.
    Itt egy dupla for ciklusos megoldást alkalmazok, mely O(n^2) futási idejű.
    Kis intervallum esetén optimális.
    """
    munchausen_numbers = []
    for i in range(0,9999+1):
        result = 0
        for n in str(i):
            if n == "0":
                result += 0
            else:
                result += int(n)**int(n)
        if i == result:
            munchausen_numbers.append(i)
    return munchausen_numbers
            

# 2. feladat
def munchausen_v2():
    """
    Ennél a függvénynél kicsit nagyobb intervallumot állítunk be:
    440000000 lesz a felső határ. (Nagyon időigényes ennek a futtatása)
    Ebben a verzióban list comprehension-nel oldom meg a feladatot, ez valamivel
    optimálisabb, mint a dupla for-ciklusos megoldás.
    """
    munchausen_numbers = []
    for i in range(0,440000000):
        if i == 0:
            munchausen_numbers.append(i)
            continue
        szamjegyek = [int(szamjegy) for szamjegy in str(i) if szamjegy != "0"] # kinyerjük a számjegyeket
        hatvanyok_osszege = sum([szamjegy**szamjegy for szamjegy in szamjegyek])
        if hatvanyok_osszege == i:
            munchausen_numbers.append(i)
    return munchausen_numbers


def main():
    print(munchausen_v1())
    print(munchausen_v2())


if __name__ == "__main__":
    main()