#!/usr/bin/env python3

from string1 import donuts, both_ends, fix_start, mix_up


def test_donuts():
    assert donuts(0) == "Fánkok száma: 0"
    assert donuts(2) == "Fánkok száma: 2"
    assert donuts(4) == "Fánkok száma: 4"
    assert donuts(10) == "Fánkok száma: sok"
    assert donuts(100) == "Fánkok száma: sok"
    assert donuts(-5) == "A megadott input kisebb, mint nulla!"
    assert donuts(-1000) == "A megadott input kisebb, mint nulla!"


def test_both_ends():
    assert both_ends("alma") == "alma"
    assert both_ends("spring") == "spng"
    assert both_ends("1234567") == "1267"
    assert both_ends("+*:-/") == "+*-/"
    assert both_ends("kutyafule") == "kule"
    assert both_ends("CHalAD") == "CHAD"
    assert both_ends("PYTHON") == "PYON"
    assert both_ends("Rózsa") == "Rósa"


def test_fix_start():
    assert fix_start("bubble") == "bu**le"
    assert fix_start("aladar") == "al*d*r"
    assert fix_start("coconut") == "co*onut"
    assert fix_start("1111111") == "1******"
    assert fix_start("  b i g b a n g ") == " *b*i*g*b*a*n*g*"
    assert fix_start("LALALA") == "LA*A*A"


def test_mix_up():
    assert mix_up("mix", "pod") == "pox mid"
    assert mix_up("dog", "dinner") == "dig donner"
    assert mix_up("turos", "teszta") == "teros tuszta"
    assert mix_up("RANTOTT", "HUS") == "HUNTOTT RAS"
    assert mix_up("123", "456") == "453 126"
    assert mix_up("  probably", "not") == "noprobably   t"
