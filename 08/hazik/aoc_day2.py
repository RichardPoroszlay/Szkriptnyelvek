#!/usr/bin/env python3


"""
Ebben a programban az AoC2017, Day2, Part1 feladata lesz megoldva.
Adott egy táblázat, melyet egy szöveges állományban tárolunk el.
A feladatunk, hogy ennek a táblázatnak a checksum értékét számoljuk ki.
Ezt úgy tesszük meg, hogy a táblázat minden sorának a legnagyobb és legkisebb értékének a 
különbségét vesszük, majd ezeket a különbségeket összeadjuk.
"""


def corruption_checksum() -> str:
    elements = []
    with open("input.txt", "r") as f:
        for line in f:
            elements.append((line.strip().replace("\t", " ")).split(" "))

    int_elements = []
    for l in elements:
        temp = []
        for e in l:
            temp.append(int(e))
        int_elements.append(temp)

    res = 0
    for l in int_elements:
        res += max(l) - min(l)
    
    return f"Result: {res}"


def main():
    print(corruption_checksum())


if __name__ == "__main__":
    main()