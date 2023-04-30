#!/usr/bin/env python3


from palindrome_v2 import is_palindrome_iterative, is_palindrome_recursive


def test_is_palindrome_iterative():
    assert is_palindrome_iterative("görög") == True
    assert is_palindrome_iterative("sajt") == False
    assert is_palindrome_iterative("apa") == True
    assert is_palindrome_iterative("madár") == False


def test_is_palindrome_recursive():
    assert is_palindrome_recursive("görög") == True
    assert is_palindrome_recursive("sajt") == False
    assert is_palindrome_recursive("apa") == True
    assert is_palindrome_recursive("madár") == False
