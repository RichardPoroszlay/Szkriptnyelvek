#!/usr/bin/env python3


"""
Ebben a programban egy eljárás segítségével fogunk kirajzolni egy 8x8-as sakktáblát,
melyen 8 darab királynő úgy lesz elhelyezve, hogy azok nem ütik egymást.
Ezt a problémát 8 királynő problémájának nevezzük.

A sakktáblát egy listában reprezentáljuk, melyben meg lesznek adva a bábuk pozíciói.
"""


def eigth_queens(positions):
    table = []

    for i in range(0, 9+1):
        row = []
        if i == 0 or i == 9:
            for j in range(0,9+1):
                if j == 0 or j == 9:
                    row.append("+")
                else:
                    row.append("-")
        elif i in range(1,8+1):
            for j in range(0,9+1):
                if j == 0 or j == 9:
                    row.append("|")
                else:
                    row.append(".")

        table.append(row)
        
    for p in positions:
        if p == 7:
            col = positions.index(p)
            table[1][col+1] = "Q"
        elif p == 6:
            col = positions.index(p)
            table[2][col+1] = "Q"
        elif p == 5:
            col = positions.index(p)
            table[3][col+1] = "Q"
        elif p == 4:
            col = positions.index(p)
            table[4][col+1] = "Q"
        elif p == 3:
            col = positions.index(p)
            table[5][col+1] = "Q"
        elif p == 2:
            col = positions.index(p)
            table[6][col+1] = "Q"
        elif p == 1:
            col = positions.index(p)
            table[7][col+1] = "Q"
        elif p == 0:
            col = positions.index(p)
            table[8][col+1] = "Q"
        else:
            print("SOMETHING WENT WRONG...")

    for row in table:
        print(" ".join(row), end="\n")


def main():
    positions = [0, 4, 7, 5, 2, 6, 1, 3]
    eigth_queens(positions)


if __name__ == "__main__":
    main()