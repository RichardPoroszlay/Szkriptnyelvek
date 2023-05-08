#!/usr/bin/env python3


"""
Szökés Alcatrazból

Ebben a feladatban 600 cella van.
Egy adott logika szerint végigmegyünk az összes cellán.
Eredményként egy listát kapunk, mely tartalmazza azon cellákat, melyek
rabjai szabadulhatnak.
"""


def cell_generator() -> list:
    cells = [False] * 600

    for i in range(1, 600 + 1):
        for j in range(i - 1, 599 + 1, i):
            cells[j] = not cells[j]

    free_people = [i + 1 for i in range(599 + 1) if cells[i]]

    return free_people


def main():
    print(cell_generator())


if __name__ == "__main__":
    main()
