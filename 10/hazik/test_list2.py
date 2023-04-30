#!/usr/bin/env python3


from list2 import remove_adjacent, list_merge


def test_remove_adjacent():
    assert remove_adjacent([1, 2, 2, 3]) == [1, 2, 3]
    assert remove_adjacent([4, 4, 5, 5, 6, 6]) == [4, 5, 6]
    assert remove_adjacent([10, 30, 50, 60, 10, 10]) == [10, 30, 50, 60]
    assert remove_adjacent([-5, -5, -5, -3, -2, -1, 0, 0, 0]) == [-5, -3, -2, -1, 0]


def test_list_merge():
    assert list_merge([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert list_merge([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]
    assert list_merge([10, 30, 50, 100], [-3, -4, -5]) == [-5, -4, -3, 10, 30, 50, 100]
    assert list_merge([5.5, 6.5, 7.5, 8.5], [2.5, 3.5, 4.5]) == [
        2.5,
        3.5,
        4.5,
        5.5,
        6.5,
        7.5,
        8.5,
    ]
    assert list_merge(["e", "f", "g", "h"], ["a", "b", "c", "d"]) == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
    ]
