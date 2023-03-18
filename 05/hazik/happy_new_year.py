#!/usr/bin/env python3


"""
Ebben a programban úgy fogjuk kiírni a 2023-at, hogy nem használunk számjegyeket a kódban.
"""


def new_year():
    """
    Egy lista segítségével hajtom végre a 2023 kiíratását, melyben különböző hosszúságú stringek vannak.
    Ezeknek a hosszúságait felhasználva egy result változóba kiírom a kért dátumot.
    """
    components = ["xx", "", "xx", "xxx"]
    result = ""
    for component in components:
        result += str(len(component))
    return result


def main():
    print(new_year())


if __name__ == "__main__":
    main()