#!/usr/bin/env python3


"""
Az adott forráskód egy modul.
A modul tartalmazza a feladat megoldását, míg a nyomtatando_oldalak.py csak a main függvényt tartalmazza
az itt látható függvény meghívásával.

A feladat az, hogy írjunk egy olyan függvényt, mely az oldalakat ilyen módon kéri be: 1, 2-5, 7, 9-14.
Ezt az inputot úgy kell kezelnie a programnak, hogy a köztes számok is jelenjenek meg egy intervallum megadásánál.

A bekero függvény fogja számunkra ezt a problémát megoldani.
"""


def bekero() -> list[int]:
    oldalszamok: list[str] = input("Adja meg a nyomtatni kívánt oldalakat: ").split(",")
    result: list[int] = []

    for e in oldalszamok:
        if "-" not in e:
            result.append(int(e))
        else:
            minmax: list[str] = e.split("-")
            for i in range(int(minmax[0]), int(minmax[1]) + 1):
                result.append(i)

    return result


if __name__ == "__main__":
    # test input: 1, 2-5, 7, 9-14
    print(bekero())
