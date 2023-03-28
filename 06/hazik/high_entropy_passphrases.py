#!/usr/bin/env python3

"""
AoC2017, Day4, Part 1 (High-Entropy Passphrases)

Az a feladatunk, hogy állapítsuk meg, hány helyes passphrase van egy input fileban.
"""


def passphrase_verifier():
    """
    A függvény egy szöveges fileból olvassa be a sorokat.
    Ezeket a sorokat aztán összehasonlítjuk azok halmazbeli megfelelőjével.
    Ha a sor és a halmaz hossza megegyezik, akkor hiteles a passphrase.
    """
    lines =  []
    with open("/home/richardpal/Desktop/passphrases.txt", "r") as f:
        for l in f:
            lines.append(l.rstrip("\n").split(" "))
    
    total = 0
    for line in lines:
        set_line = set(line)
        if len(line) == len(set_line):
            total += 1
    return total


def main():
    print(f"A helyesen megadott passphrase-ek száma: {passphrase_verifier()}")
    

if __name__ == "__main__":
    main()