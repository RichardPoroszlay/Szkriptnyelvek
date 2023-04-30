#!/usr/bin/env python3


"""
A. match_ends
Bemenet: sztringek listája. Számoljuk meg, hogy a bemenetben
hány olyan sztring van, melynek a hossza legalább 2 s az
első karaktere egyezik az utolsó karakterével. A visszatérési
érték ezen feltételeket kielégítő sztringek száma legyen.
Megjegyzés: Pythonban inkrementálásra a ++ helyett a += operátort használjuk.
"""


def match_ends(words: list[str]) -> int:
    total = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            total += 1
    return total


"""
B. front_x
Bemenet: sztringek listája. Egy olyan listával térjünk vissza,
melyben a szavak rendezve vannak, viszont az 'x'-szel kezdődő szavak
kerüljenek előre.
Példa: ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] bemenet esetén
az eredmény: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].
Tipp: használhatunk 2 listát is, melyeket külön-külön rendezünk, majd
      egyesítjük őket.
"""


def front_x(words: list[str]) -> list[str]:
    x_first: list[str] = []
    ordered_list: list[str] = []

    for word in words:
        if word[0] == "x":
            x_first.append(word)
        else:
            ordered_list.append(word)

    ordered_list.sort()
    x_first.sort()

    return x_first + ordered_list
