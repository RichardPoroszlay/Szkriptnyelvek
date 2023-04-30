#!/usr/bin/env python3


"""
Az alábbi függvény két szó Hamming-távolságát hivatott kiszámolni.
Két szó Hamming-távolsága a szavakban lévő különböző karakterek összege.
"""


def hamming(word1: str, word2: str) -> str:
    if len(word1) != len(word2):
        return "Nem egyezik a két szó hossza!"
    elif word1 == word2:
        return "A két szó megegyezik egymással! A Hamming-távolságuk: 0"

    different_chars = 0
    for i in range(0, len(word1)):
        if word1[i] != word2[i]:
            different_chars += 1

    return f"A két szó Hamming-távolsága: {different_chars}"
