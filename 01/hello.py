#!/usr/bin/env python3

# comment


def main():
    print("Hello,")
    print("World!")
    if True:
    	print("igaz")

# Ha ez a file egy library lenne és egy másik file-ban használnánk, akkor nem hívódna meg az alábbi miatt a függvény
if __name__ == "__main__":    
    main()
    
