#!/usr/bin/env python3


"""
Lista elemeinek szorzata

Írjunk függvényt, mely kap egy egészeket tartalmazó listát s visszaadja a listában lévő elemek szorzatát.

Megjegyzés

Definíció szerint egy üres lista elemeinek a szorzata 1. Hasonlóképpen, egy üres lista elemeinek az összege 0.
"""


def product(numbers: list[int]) -> int:
    if len(numbers) == 0:
        return 1
    total = 1
    for number in numbers:
        total *= number
    return total
