#!/usr/bin/env python3


# Lista elemeinek szorzata

# Írjunk függvényt, mely kap egy egészeket tartalmazó listát s visszaadja a listában lévő elemek szorzatát.

# Megjegyzés

# Definíció szerint egy üres lista elemeinek a szorzata 1. Hasonlóképpen, egy üres lista elemeinek az összege 0.


def product(numbers):
    if len(numbers) == 0:
        return 1
    total = 1
    for number in numbers:
        total *= number
    return total


def main():
    list1 = [1, 2, 3, 4, 5]
    print("Production of numbers of list1: " + str(product(list1)))

    list2 = [3, 5, 8, 15, 33, 81, 9, 4, 38, 53]
    print("Production of numbers of list2: " + str(product(list2)))

    list3 = [-1, -27]
    print("Production of numbers of list3: " + str(product(list3)))

    list4 = [-3, 9, 2]
    print("Production of numbers of list4: " + str(product(list4)))

    list5 = []
    print("Production of numbers of list5: " + str(product(list5)))


if __name__ == "__main__":
    main()