#!/usr/bin/env python3

import sys    # parancssori argumentumokhoz való hozzáférés


def hello(s):
    if s == "Batman" or s == "Robin":   # lehetne zárójelezni is, de preferencia miatt nem indokolt
        print("Denevérveszély")
    else:
        print("Hello, " + s + "!")    


def main():
    print(sys.argv)     # ez egy tömb, tartalmazza a parancssori argumentumokat
    name = sys.argv[1]
    hello(name)
    
  
if __name__ == "__main__":
    main()

