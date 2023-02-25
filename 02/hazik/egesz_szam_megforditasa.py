#!/usr/bin/env python3

#Írjunk függvényt, mely kap egy pozitív egész számot, 
# s visszatérési értékként a szám fordítottját adja vissza mint egész számot. 

# Példa: 1977 --> 7791; 12568 --> 86521.

# (Feltételezhetjük, hogy az eredeti szám nem 0-ra végződik.) 

# v1 --> ezzel a megoldással nem kell átkonvertálni string-be a paramétert
def reverse_number_v1(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n //= 10
    return r


# v2 (szorgalmi)  # itt stringként return-öljük
def reverse_number_v2(n):
    n_str = str(n)
    return n_str[::-1]


def main():
    print(reverse_number_v1(987654321))
    print(reverse_number_v2(54321))


if __name__ == "__main__":
    main()