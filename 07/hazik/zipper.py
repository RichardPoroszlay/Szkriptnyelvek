#!/usr/bin/env python3

"""
Ebben a feladatban a zip() függvény segítségével ASCII érték-kód
párokat íratok ki a zip() függvény segítségével.

Ha a codes változó csak egy range lenne, s nem alakítanánk azt át listává,
akkor az ord() függvény csak az 'a' karakter ASCII kódját adná vissza. Ilyenkor
nem tudna a for-ciklus semmit sem bejárni.

Azért kell listává alakítani, hogy a zip() függvény
létre tudjon hozni párokat.
"""


def main():
    chars = "abcdefghijklmnopqrstuvwxyz"
    codes = list(range(ord('a'), ord('z')+1))

    for t in zip(chars, codes):
        print(t)


if __name__ == "__main__":
    main()