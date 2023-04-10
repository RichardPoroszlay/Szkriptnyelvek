#!/usr/bin/env python3


"""
Ebben a programban implementáljuk a Sphere (gömb) osztályt.
A lenti implementáció tartalmaz operátor túlterhelést, továbbá tartalmazza a test térfogatának és területének kiszámítását.
"""


import math


class Sphere:
    def __init__(self, radius):
        self.radius = radius
    

    def __str__(self) -> str:
        return f"Sphere with radius {self.radius}"
    

    def __repr__(self) -> str:
        return f"Sphere({self.radius})"
    

    def __lt__(self, other) -> str:
        return f"{self} is less than {other}: {self.radius < other.radius}"
    

    def __le__(self, other) -> str:
        return f"{self} is less or equal than {other}: {self.radius <= other.radius}"
    

    def __gt__(self, other) -> str:
        return f"{self} is greater than {other}: {self.radius > other.radius}"
    

    def __ge__(self, other) -> str:
        return f"{self} is greater or equal than {other}: {self.radius >= other.radius}"
    
    
    def volume(self) -> str:
        return f"Volume of {self}: {(4/3) * math.pi * self.radius ** 2}"
    

    def surface_area(self) -> str:
        return f"Surface Area of {self}: {4 * math.pi * self.radius ** 2}"
    

def main():
    # test
    s1 = Sphere(13)
    print(s1.volume())
    print(s1.surface_area())

    s2 = Sphere(24)
    print(s2.volume())
    print(s2.surface_area())

    s3 = Sphere(24)

    print(s1 < s2)
    print(s1 > s2)
    print(s2 < s3)
    print(s2 <= s3)


if __name__ == "__main__":
    main()