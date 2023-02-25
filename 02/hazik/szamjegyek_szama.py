#!/usr/env/bin python3

# Hány számjegyből áll 2^256?

# Tipp: hatványozásra a ** operátort használjuk, pl. 2**3 = 8. A túlcsordulástól nem kell félni :)


def length_of_num():
    num = 2**256    # 78 a hossza
    str_num = str(num)
    total = 0
    for i in str_num:
        total += 1
    return total


def main():
    print(length_of_num())


if __name__ == "__main__":
    main()