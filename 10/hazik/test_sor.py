#!/usr/bin/env python3


from sor import Sor


def test_ures():
    test_sor1 = Sor()
    assert test_sor1.ures() == True

    test_sor2 = Sor()
    test_sor2.betesz(1)
    assert test_sor2.ures() == False

    test_sor3 = Sor()
    test_sor3.betesz(1)
    test_sor3.betesz(2)
    test_sor3.betesz(3)
    assert test_sor2.ures() == False


def test_meret():
    test_sor1 = Sor()
    assert test_sor1.meret() == 0

    test_sor2 = Sor()
    test_sor2.betesz(1)
    assert test_sor2.meret() == 1

    test_sor3 = Sor()
    test_sor3.betesz(1)
    test_sor3.betesz(2)
    assert test_sor3.meret() == 2


def test_kivesz():
    test_sor1 = Sor()
    test_sor1.betesz(1)
    test_sor1.betesz(2)
    test_sor1.betesz(3)
    assert test_sor1.kivesz() == 1

    test_sor2 = Sor()
    test_sor2.betesz(7)
    test_sor2.betesz(21)
    test_sor2.betesz(4)
    assert test_sor2.kivesz() == 7
