#!/usr/bin/env python3


"""
Ebben a feladatban a haladó rendezéssel foglalkozunk.
"""


# 1. feladat
def my_func1(t: tuple) -> tuple:
    return t[-1]


# 2. feladat
def my_func2(user: str) -> int:
    return int(user.split(":")[0])


# 3. feladat
def my_func3(matrix: list) -> list:
    return matrix[:][1]


def main():
    # 1. feladat
    data = [
        (1, "Albany", "NY", 162692),
        (3, "Allegany", "NY", 11986),
        (121, "Wyoming", "NY", 8722),
        (123, "Yates", "NY", 5094),
    ]

    print(sorted(data, key=my_func1))

    # 2. feladat
    users = ["10:User1", "80:User2", "100:User3", "00:User4", "75:User4", "45:User5"]

    res = sorted(users, key=my_func2, reverse=True)

    for u in res:
        print(u)

    # 3. feladat
    li = [[2, 6], [1, 3], [5, 4]]
    print(sorted(li, key=my_func3))


if __name__ == "__main__":
    main()
