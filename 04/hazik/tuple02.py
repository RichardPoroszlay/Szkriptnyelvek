#!/usr/bin/env python3

import math

# c^2 = a^2 + b^2
def distance(p1, p2):
    a = (p2[0] - p1[0])**2
    b = (p2[1] - p1[1])**2
    c = a + b
    return math.sqrt(c)


def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print('A ket pont kozti tavolsag:', distance(p1, p2))

#############################################################################

if __name__ == "__main__":
    main()
