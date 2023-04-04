#!/usr/bin/env python3


"""
A feladatban a TEXT globális változóban lévő bináris kódban lévő szöveget
kell dekódolnunk. Ehhez egy solver nevű függvényt használok, ahol
binárisból decimálisba váltom a számokat, s a decimális számokhoz rendelt
ASCII betűket visszafejtem.
"""


TEXT = """
01111001 01101111
01110101 01110100
01110101 00101110
01100010 01100101
00101111 01100100
01010001 01110111
00110100 01110111
00111001 01010111
01100111 01011000
01100011 01010001
"""


def solver(text):
    binary = text.split()
    decimal = []
    for e in binary:
        decimal.append(int(e, 2))
    
    result = ""
    for i in decimal:
        result += chr(i)
    return result


def main():
    print(solver(TEXT))


if __name__ == "__main__":
    main()