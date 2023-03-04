#!/usr/bin/env python3


def cleaner(word):
    clean_word = " ".join(word.split())
    return clean_word


def main():
    # test
    print(cleaner("192.20.246.138:\n 6666"))
    print(cleaner("206.130.99.82:\n8080"))
    print(cleaner("\nHey!\tHow are you doing?"))

if __name__ == "__main__":
    main()