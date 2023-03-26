#!/usr/bin/env python3

"""
Ebben a programban össze fogunk hasonlítani két stringet, s megállapítjuk
hogy ezen stringek anagrammák-e.

Egy szó akkor anagrammája egy másik szónak, ha az elsőnek a sorrendjeinek megváltoztatásával
megkapjuk a második szót.
"""


def normalize(word):
    """
    A szóközök nem számítanak az anagrammánál, továbbá nincs különbség a kis- és nagybetűk közt.
    Ezzel a függvénnyel a szóból kiszedjük az összes whitespace-t, illetve kisbetűssé alakítjuk.
    """
    result = word.lower().strip().replace(" ", "")
    return result


def anagramma(word1, word2):
    """
    Egy egyszerű trükk segítségével könnyen megállapíthatjuk két szóról, hogy az egyik
    anagrammája-e egy másiknak.
    Csupán annyit kell tennünk, hogy a szavak betűit sorrendbe helyezzük, s ha azok sorrendje
    megegyezik, akkor tudhatjuk, hogy anagrammákról van szó.
    """
    if sorted(word1) == sorted(word2):
        return f"A '{word1}' szó anagrammája a '{word2}' szónak!"
    else:
        return f"A '{word1}' szó NEM anagrammája a '{word2}' szónak!"


def main():
    # test
    print(anagramma("listen", "silent"))
    print(anagramma(normalize("A gentleman"), normalize("Elegant man")))
    print(anagramma(normalize("Clint Eastwood"), normalize("Old west action")))
    print(anagramma("dormitory", normalize("dirty room")))

    print(anagramma("kutya", "macska"))
    print(anagramma("python", "java"))
    print(anagramma("1234", "5478"))


if __name__ == "__main__":
    main()