#!/usr/bin/env python3


def szamjegyek_osszege(num):
    """
    A függvény egy bemeneti paraméterként kapott szám számjegyeinek összegét számolja ki.
    A bemeneti paraméter lehet kifejezés is.
    """
    result = 0
    for n in str(num):
        result += int(n)
    return f"{num} számjegyeinek összege: {result}"


def main():
    # test
    print(szamjegyek_osszege(2**1000))


if __name__ == "__main__":
    main()