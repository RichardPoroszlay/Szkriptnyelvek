#!/usr/bin/env python3


def is_palindrome_iterative(word):
    mid_point = len(word) // 2
    for i in range(0, mid_point):
        left_side = word[i]
        right_side = word[len(word)-i-1]
        if left_side != right_side:
            return False
    return True


def is_palindrome_recursive(word):
    if len(word) < 2:
        return True
    first_letter = word[0]
    last_letter = word[-1]
    if first_letter == last_letter:
        middle_word = word[1:len(word)-1]
        return is_palindrome_recursive(middle_word)
    else:
        return False
