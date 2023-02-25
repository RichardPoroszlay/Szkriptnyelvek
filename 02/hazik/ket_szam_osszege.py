#!/usr/bin/env python3

# Olvassunk be két egész számot s írjuk ki a két szám összegét.

# A) változat:

# A két egész számot parancssori argumentumként adjuk meg. 
# Ha a felhasználó nem adja meg mindkét számot, akkor írjunk ki egy hibaüzenetet! 

# B) változat:

# A két egész számot interaktív módon kérjük be.


# (A) változat
def sum_of_two_numbers_v1(a, b):
    return a + b


# (B) változat
def sum_of_two_numbers_v2():
    print("-----Két szám összeadása-----")
    num1 = input("Adja meg az első számot: ")
    num2 = input("Adja meg a második számot: ")
    return int(num1) + int(num2)


def main():
    print(sum_of_two_numbers_v1(10, 10))
    print(sum_of_two_numbers_v2())


if __name__ == "__main__":
    main()