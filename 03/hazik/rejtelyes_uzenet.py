#!/usr/bin/env python3

# ASCII kódtábla szerint kell dekódolni a szöveget

CODED_TEXT = """
    Cbcq Dgyk!

    Dmeybh kce cew yrwyg hmrylyaqmr:
    rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

    Aqmimjjyi:

    Ynyb
"""


def decoder(text):
    decoded_text = ""
    for letter in text:
        if letter.isalpha():
            if letter == 'Y':
                decoded_text += 'A'
            elif letter == 'y':
                decoded_text += 'a'
            else:
                decoded_text += chr(ord(letter)+2)
        else:
            decoded_text += letter
    return decoded_text;


def main():
    print(decoder(CODED_TEXT))


if __name__ == "__main__":
    main()