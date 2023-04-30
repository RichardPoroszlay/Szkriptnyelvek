#!/usr/bin/env python3


"""
D.
Bemenet: számok rendezett listája.
Kimenet: a bementből távolítsuk el az ismétlődéseket, vagyis az
eredményben egy szám csak egyszer szerepeljen.
Példa: [1, 2, 2, 3] -> [1, 2, 3].
Készíthetünk egy új listát, vagy módosíthatjuk a bemeneti listát is.
"""


def remove_adjacent(nums: list[int]) -> list[int]:
    temp = []
    for number in nums:
        if number not in temp:
            temp.append(number)
    return temp


"""
E.
Bemenet: két lista, mindkettőben az elemek növekvő sorrendbe rendezve.
Kimenet: egy összefésült lista, melyben az elemek rendezve szerepelnek.
"""


def list_merge(
    list1: list[str] | list[int] | list[float],
    list2: list[str] | list[int] | list[float],
) -> list[str] | list[int] | list[float]:
    ordered_list = sorted(list1 + list2)
    return ordered_list
