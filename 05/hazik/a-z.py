#!/usr/bin/env python3

import sys


"""
Ebben a programban a-tól z-ig kiírjuk a betűket
"""


def a_to_z():
    """
    Ez a függvény visszaadja a-tól z-ig a betűket string formában.
    A karakterek kinyeréséhez az ASCII kódtáblát használjuk.
    """
    if sys.argv[0].endswith("z-a.py"):
        concat = ""
        for c in range(122, 95+1, -1):
            concat += chr(c)
        return concat
    else:
         concat = ""
         for c in range(97, 122+1):
            concat += chr(c)
         return concat


def main():
    print(a_to_z())


if __name__ == "__main__":
    main()
