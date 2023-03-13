#!/usr/bin/env python3


def szamlalo(start, end):
    szamok = list(range(start, end+1))
    negyzetosszeg = sum([szam*szam for szam in szamok])
    osszeg_negyzet = sum(szamok)**2

    return "Result: " + osszeg_negyzet - negyzetosszeg


def main():
    print(szamlalo(1,100)) # 25164150


if __name__ == "__main__":
    main()
