#!/usr/bin/env python3


"""
Ebben a feladatban olyan szavakat keresünk, melyekben a j, s, u, n betűk
a fent leírt sorrendben szerepelnek.
"""


import re


def main():
    # Szószedet betöltése
    with open("corpus.txt", encoding="utf-8") as f:
        corpus = f.read()

    # Keresés a szószedetben
    matches = re.findall(r"\b\w*(j.*s.*u.*n)\w*\b", corpus)

    # Találatok kiíratása
    for match in matches:
        print(match)


if __name__ == "__main__":
    main()
