#!/usr/bin/env python3

import pygyak

# modulok importálásának sorrendje számít a csillaggal való importálás esetén

"""
Az óra első feladataként kiíratjuk a 100-nál kisebb prímeket, majd
a 200-nál kisebb prímek összegét.
"""


def main():
    # ex1
    for i in range(1,100):
        if pygyak.is_prime(i):
            print(i)
    
    # ex2
    res = 0
    for i in range(1,200):
        if pygyak.is_prime(i):
            res += i
    print(f"200-nál kisebb prímek összege: {res}")

    # ex3
    print(pygyak.is_prime(5))
    print(pygyak.hello())


if __name__ == "__main__":
    main()