#!/usr/bin/env python3


"""
Ebben a feladatban azoknak a számoknak az összegét keressük,
melyek kisebbek, mint egy millió, továbbá bináris és decimális számrendszerben
is palindrómok.

A feladat megoldásához 2 függvényt fogok használni arra, hogy meghatározzam, hogy
az adott számok palindrómok-e a számrendszerekben, majd a test függvényben
ezeket kombinálom, hogy a keresett számok összegét megkapjam.
"""


def binaris_palindrom(num: int) -> bool:
    binary = bin(num)[2:]
    if binary[0] == "0":
        return (
            False  # a feladat meghatározta, hogy a bináris verzió sem kezdődhet 0-val
        )

    if binary == binary[::-1]:
        return True


def decimalis_palindrom(num: int) -> bool:
    if str(num)[0] == 0:
        return False  # a decimális verzió sem kezdődhet 0-val
    if str(num) == str(num)[::-1]:
        return True
    return False


def test() -> int:
    total = 0
    for i in range(0, 1000000):
        if binaris_palindrom(i) and decimalis_palindrom(i):
            total += i
    return total


def main():
    print(f"Eredmény: {test()}")


if __name__ == "__main__":
    main()
