#!/usr/bin/env python3


def logical_xor(str1, str2):
    if (bool(str1) ^ bool(str2)):
        return "Erre a két változóra igaz az XOR művelet."
    else:
        return "Erre a két változóra NEM igaz az XOR művelet."


def main():
    str1 = "python"
    str2 = None
    str3 = "cat"
    str4 = "dog"
    str5 = ""
    str6 = None
    print(logical_xor(str1, str2))
    print(logical_xor(str3, str4))
    print(logical_xor(str5, str6))


if __name__ == "__main__":
    main()