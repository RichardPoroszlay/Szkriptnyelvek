#!/usr/bin/env python3


"""
Ebben a programban implementáljuk az Ellipse (elipszis) osztályt.
A lenti implementáció tartalmaz operátor túlterhelést, továbbá a test területének, kerületének és excentrikusságának kiszámítását.
"""


import math


class Ellipse:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def __str__(self) -> str:
        return f"Ellipse with semi-major axis {self.a} and semi-minor axis {self.b}"


    def __repr__(self) -> str:
        return f"Ellipse({self.a}, {self.b})"
     

    def __lt__(self, other) -> str:
        return f"{self} is less than {other}: {(self.a * self.b) < (other.a * other.b)}"
     

    def __le__(self, other) -> str:
        return f"{self} is less or equal than {other}: {(self.a * self.b) <= (other.a * other.b)}"
     

    def __gt__(self, other) -> str:
        return f"{self} is greater than {other}: {(self.a * self.b) > (other.a * other.b)}"
     

    def __ge__(self, other) -> str:
        return f"{self} is greater or equal than {other}: {(self.a * self.b) >= (other.a * other.b)}"
     

     # terulet
    def area(self) -> str:
        return f"Area of {self}: {math.pi * self.a * self.b}"
     

     # kerulet
    def circumference(self) -> str:
        h = ((self.a - self.b) / (self.a + self.b)) ** 2
        return f"Circumreference of {self}: {math.pi * (self.a + self.b) * (1 + ((3 * h) / (10 + math.sqrt(4 - (3 * h)))))}"


    # excentrikusság
    def eccentricity(self) -> str:
        return f"Eccentricity of {self}: {math.sqrt(1 - ((self.b ** 2) / (self.a ** 2)))}"
    

def main():
    # test
    e1 = Ellipse(25, 12)
    e2 = Ellipse(4, 8)
    e3 = Ellipse(4, 8)

    print(e1.area())
    print(e1.circumference())
    print(e1.eccentricity())

    print(e2 < e1)
    print(e2 <= e3)
    print(e2 > e1)
    print(e2 >= e3)


if __name__ == "__main__":
    main()