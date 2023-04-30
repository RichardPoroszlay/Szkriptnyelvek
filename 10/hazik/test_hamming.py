#!/usr/bin/env python3


from hamming import hamming


def test_hamming():
    assert hamming("toned", "roses") == "A két szó Hamming-távolsága: 3"
    assert hamming("moose", "goose") == "A két szó Hamming-távolsága: 1"
    assert hamming("hello", "ballo") == "A két szó Hamming-távolsága: 2"
    assert hamming("angry", "birds") == "A két szó Hamming-távolsága: 5"
    assert (
        hamming("hey", "hey")
        == "A két szó megegyezik egymással! A Hamming-távolságuk: 0"
    )
    assert hamming("ooo", "oooo") == "Nem egyezik a két szó hossza!"
    assert hamming("iiiii", "aaa") == "Nem egyezik a két szó hossza!"
