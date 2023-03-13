#!/usr/bin/env python3


# the parameter must be an odd number
def diamond_drawer(height):

    if height < 0:
        return "Number can't be less than zero!"
    elif height % 2 == 0:
        return "Number of height isn't odd! It's wrong!"
    result = ""
    counter_inc = 1
    while counter_inc <= height:
        symbol = '*'
        symbol *= counter_inc
        result += symbol.center(height) + '\n'
        counter_inc += 2

    counter_dec = height
    while counter_dec >= 1:
        counter_dec -= 2
        symbol = '*'
        symbol *= counter_dec
        result += symbol.center(height) + '\n'
    return result


def main():
    print(diamond_drawer(3))
    print(diamond_drawer(5))
    print(diamond_drawer(7))
    print(diamond_drawer(27))
    print(diamond_drawer(2))
    print(diamond_drawer(12))
    print(diamond_drawer(0))
    print(diamond_drawer(-32))
    print(diamond_drawer(-3))


if __name__ == "__main__":
    main()