#!/usr/bin/env python3


"""
Ebben a programban két függvény segítségével meghatározzuk egy harmadik függvényben,
hogy egy adott szám prímszám-e, s egyben palindróm.
"""


def is_palindrome(s: str) -> bool:
    """
    A függvény eldönti, hogy a szám (vagy szó) palindróm-e vagy sem.
    """
    if s == s[::-1]:
        return True
    return False


def is_prime(n: int) -> bool:
    """
    A függvény eldönti, hogy egy szám prím-e vagy sem.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    maxi = n**0.5 + 1
    while i <= maxi:
        if n % i == 0:
            return False
        i += 2

    return True


def test(n: int) -> int:
    for i in range(n, 1000000):
        if is_palindrome(str(i)) and is_prime(n):
            return i


def main():
    print(f"Az adott szám prím és palindróm: {test(31) == 101}")  # False
    print(f"Az adott szám prím és palindróm: {test(130) == 131}")  # False
    print(f"Az adott szám prím és palindróm: {test(131) == 131}")  # True
    print(f"Az adott szám prím és palindróm: {test(1977) == 10301}")  # False
    print(f"Az adott szám prím és palindróm: {test(11) == 11}")  # True
    print(f"Az adott szám prím és palindróm: {test(404) == 404}")  # False


if __name__ == "__main__":
    main()
