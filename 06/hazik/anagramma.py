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


# triviális megoldás
def anagramma_v1(word1, word2):
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


# nem triviális megoldás
def anagramma_v2(word, word_list):
    """
    Ez a függvény egy kevésbé triviális megoldás egy anagramma megtalálásához.
    Egy szótár segítségével fogjuk megállapítani, hogy mikor anagramma egy szó.
    Hogy ha a bemeneti paraméter "word" egy anagramma, akkor az előállított "word_list"
    listában ennek a szónak a rendezett változata megtalálható.
    A függvény egy két elemű listát ad vissza, melyben két anagramma található.
    """
    word = normalize(word)
    anagrammak = {}

    for w in word_list:
        w = normalize(w)
        if sorted(word) == sorted(w):
            anagrammak[w] = "Anagramma"
    
    return list(anagrammak.keys())


def main():
    # test
    print(anagramma_v1("listen", "silent"))
    print(anagramma_v1(normalize("A gentleman"), normalize("Elegant man")))
    print(anagramma_v1(normalize("Clint Eastwood"), normalize("Old west action")))
    print(anagramma_v1("dormitory", normalize("dirty room")))

    print(anagramma_v1("kutya", "macska"))
    print(anagramma_v1("python", "java"))
    print(anagramma_v1("1234", "5478"))

    word_list = ["listen", "silent", "elbow", "below", "state", "taste", "fairy tales", "rail safety", "A gentleman", "Elegant man", "Clint Eastwood", "Old west action", "dormitory", "dirty room"]
    print(anagramma_v2("listen", word_list))
    print(anagramma_v2("A gentleman", word_list))
    print(anagramma_v2("Clint Eastwood", word_list))
    print(anagramma_v2("dormitory", word_list))
    

if __name__ == "__main__":
    main()