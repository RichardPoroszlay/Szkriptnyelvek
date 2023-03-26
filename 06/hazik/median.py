#!/usr/bin/env python3

"""
Ebben a programban adott lesz egy lista, melynek a medián értékét szeretnénk kiszámolni
egy függvény segítségével.
"""


def median(nums):
    """
    A függvény bemeneti paraméterként egy egész számokkal ellátott listát kap.
    Ezen függvény segítségével kiszámoljuk, hogy mi a kapott lista mediánja.
    """
   
    ordered = sorted(nums)
    
    if len(ordered) % 2 == 0:
        return f"{nums} mediánja: {(ordered[int(len(ordered)/2)] + ordered[int(len(ordered)/2-1)]) / 2}"
    else:
        return f"{nums} mediánja: {ordered[len(ordered)//2]}"
    

def main():
    # test
    nums1 = [1,2,3,4]
    print(median(nums1))
    nums2 = [3, 1, 2, 5, 3]
    print(median(nums2))
    nums3 = [3, 1, 2, 5, 3]
    print(median(nums3))
    nums4 = [1, 300, 2, 200, 1]
    print(median(nums4))
    nums5 = [3, 6, 20, 99, 10, 15]
    print(median(nums5))



if __name__ == "__main__":
    main()