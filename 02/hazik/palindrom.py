# Írjunk függvényt, mely egy sztringről eldönti, hogy palindróm-e. Egy karaktersorozatot akkor nevezünk palindrómnak, 
# ha visszafelé olvasva megegyezik az eredeti karaktersorozattal, pl.: görög.

#!/usr/bin/env python3


def is_palindrome(word):
    reverse = word[::-1]
    if word == reverse:
        return True
    return False


def main():
    # testing purposes
    print(is_palindrome("kutya"))
    print(is_palindrome("görög"))
    print(is_palindrome("alma"))
    print(is_palindrome("apa"))


if __name__ == "__main__":
    main()