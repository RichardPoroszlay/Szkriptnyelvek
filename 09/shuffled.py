#!/usr/bin/env python3

import random


def shuffled(li):
    res = li[:]
    random.shuffle(res)
    return li, res


def get_random_elem_from(li):
    return li[random.randrange(0, len(li))]


def main():
    pass


if __name__ == "__main__":
    li = [1,2,3,4,5]
    print(shuffled(li))
    print(get_random_elem_from(li))
