#!/usr/bin/env python3


from product import product


def test_product():
    assert product([1, 2, 3, 4, 5]) == 120
    assert product([3, 5, 8, 15, 33, 81, 9, 4, 38, 53]) == 348845745600
    assert product([-1, -27]) == 27
    assert product([-3, 9, 2]) == -54
    assert product([]) == 1
