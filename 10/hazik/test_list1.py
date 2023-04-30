#!/usr/bin/env python3

from list1 import match_ends, front_x


def test_match_ends():
    assert match_ends(["alma", "körte", "szilva"]) == 1
    assert match_ends(["101", "404", "050", "11", "9"]) == 4
    assert match_ends(["KéK", "kÉk", "Kék"]) == 2


def test_front_x():
    assert front_x(["mix", "xyz", "apple", "xanadu", "aardvark"]) == [
        "xanadu",
        "xyz",
        "aardvark",
        "apple",
        "mix",
    ]
    assert front_x(["a", "d", "c", "k", "x", "b"]) == ["x", "a", "b", "c", "d", "k"]
    assert front_x(["+", "-", "x", "/"]) == ["x", "+", "-", "/"]
    assert front_x(["A", "B", "C", "X", "x"]) == ["x", "A", "B", "C", "X"]
