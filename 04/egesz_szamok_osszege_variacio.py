#!/usr/bin/env python3


def digit_sum(start, end):
    elements = []
    for i in range(start, end+1):
        elements.append(str(i))
    merged = "".join(elements)
    
    splitted_elements = []
    for i in merged:
        splitted_elements.append(int(i))
    total = sum(splitted_elements)
    return total


def main():
    print("Számjegyek összege: " + str(digit_sum(1,100)))


if __name__ == "__main__":
    main()