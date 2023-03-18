#!/usr/bin/env python3


def new_year():
    components = ["xx", "", "xx", "xxx"]
    result = ""
    for component in components:
        result += str(len(component))
    return result


def main():
    print(new_year())


if __name__ == "__main__":
    main()