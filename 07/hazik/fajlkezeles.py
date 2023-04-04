#!/usr/bin/env python3


"""
A feladatban egy forrásfájlból eltávolítjuk azokat a sorokat,
melyek # karakterrel kezdődnek, továbbá azokat a sorokat,
melyek indentálva vannak, s # karakterrel kezdődnek.

Az eredmény file neve string_clean.py.
"""


def main():
    with open("/home/richardpal/Desktop/Szkriptnyelvek/07/hazik/string1.py", "r") as f:
        lines = f.readlines()
    
    with open("/home/richardpal/Desktop/Szkriptnyelvek/07/hazik/string_clean.py", "w") as f:
        for line in lines:
            if not (line.startswith('#') or line.lstrip().startswith('#')):
                f.write(line)
    

if __name__ == "__main__":
    main()