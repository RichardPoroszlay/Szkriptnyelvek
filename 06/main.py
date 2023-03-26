#!/usr/bin/env python3

# Dictionary adatszerkezet: kulcs-érték párok (hash-map)
# Kulcsok egyediek, minden kulcshoz tartozik egy érték, ami bármi lehet (None is)
# A kulcsnak immutable dolognak kell lennie (szám, string, tuple)
# KeyError --> ha olyan kulcsra hivatkozok, amely nem létezik

# Dictionary is egy objektum, vannak metódusai
# d.get()
# d.keys() --> egy iterátor, visszaadja a kulcsokat egy dictionaryből
# d.values() --> szintén iterátor, értékeket adja vissza
# d.items()

# for w in words:
#   d[w] = d.get(w,0) + 1

# Fájlkezelés
# open() --> vissza fog adni egy file handler objektumot
# close() --> ha nem kell már a file, akkor ezt a metódust hívjuk meg
# for earch ciklussal soronként be tudjuk olvasni az állomány tartalmát
# 3 mód: read, write, append
# read csak olvas, write felülírja, azaz elveszik a tartalom, append a tartalomhoz ír hozzá
# .readlines()
# .read()


def main():
    d = {}  # üres szótár
    d["a"] = "alfa" # "a" kulcshoz tartozik az "alfa" string
    d["b"] = "beta"
    d["g"] = "gamma"
    print(d)

    d.get("a")  # visszaadja az a kulcson lévő értéket
    d.get("x", "nincs benne")   # ha nincsen benne adott kulcs, akkor azt jelzi
    
    for k in d.keys():
        print(k)

    for k, v in d.items():
        print(k, "-->", v)

    f1 = open(INPUT, 'r')
    to = open(OUTPUT, 'w')
    for line in f1:
        to.write(output)
    f1.close()
    to.close()


if __name__ == "__main__":
    main()