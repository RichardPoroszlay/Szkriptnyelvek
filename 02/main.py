#!usr/bin/env python3

#define MAX 100

PI = 3.14169

def hello(name, color, what):
    # geza, kek az eg!
    # v1
    print("{0}, {1} az {2}!".format(name, color, what)) # string formatting
    # v2
    print("{}, {} az {}!".format(name, color, what)) # string formatting --> ennél az argumentumok sorrendje számít
    # v3
    print("{n}, {c} az {w}!".format(n=name, c=color, w=what)) # string formatting --> aliasokkal (alias neve lehet a változó neve is akár)
    # v4
    print(f"1 + 1 = {1+1}") # string formatting --> beágyazott kifejezést kiértékeli, DE: kell az elejére az 'f'
    # formázott stringbe nem érdemes komplex kifejezéseket írni, egy változóba írd azt helyette
    print(f"{name.capitalize()}, {color} az {what}!")
    
    # valami[0:3]    --> kiírja a valami string indexeit 0-tól 2-ig     valami[:3] ugyan ezt a hatást éri el

def main():
    hello("geza", "kek", "eg")
    print("-" * 40)
    hello("peti", "piros", "auto")


if __name__ == "__main__":
    main()