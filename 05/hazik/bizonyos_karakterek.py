#!/usr/bin/env python3


"""
Ebben a programban az opcionális paraméterek használatát gyakoroljuk.
"""


def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """
    A függvény kap egy stringet paraméterként, továbbá van egy
    opcionális paramétere, mely azokat a karaktereket tartalmazza, amelyek
    szerepelhetnek a beírt stringben.
    Defaultként nagy betűk + számok vannak átadva, azonban ez felülírható.
    A függvény egy validált stringet ad vissza.
    """
    result = ""
    for c in text:
        if c in chars:
            result += c
    return result


def main():
    # test
    print(valid("Barking!"))
    print(valid("KL754", "0123456789"))
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))


if __name__ == "__main__":
    main()