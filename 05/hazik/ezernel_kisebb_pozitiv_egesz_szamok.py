#!/usr/bin/env python3


"""
A program kiszámolja az olyan számok összegét, melyek 1000-nél kisebbek, továbbá
vagy 3 vagy 5 többszörösei.
"""


def ezernel_kisebb_pozitiv_egesz_szamok():
    """
    List comprehension segítségével kiszámoljuk az 1000-nél kisebb számok összegét,
    melyek 3 vagy 5 többszörösei.
    """
    elements = sum([n for n in range(1, 999+1) if n % 3 == 0 or n % 5 == 0])
    print(f"1000-nél kisebb számok összege, melyek 3 vagy 5 többszörösei: {elements}")
    

def main():
    ezernel_kisebb_pozitiv_egesz_szamok()


if __name__ == "__main__":
    main()