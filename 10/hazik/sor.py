#!/usr/bin/env python3


"""
Ebben az állományban a Sor adatszerkezet implementációját valósítom meg.
"""


class Sor:
    def __init__(self):
        self.s = []

    
    def betesz(self, n: int):
        self.s.append(n)
    

    def kivesz(self) -> int:
        if len(self.s) == 0:
            return None
        return self.s.pop(0)

    
    def ures(self) -> bool:
        if len(self.s) == 0:
            return True
        return False
    

    def meret(self) -> int:
        return len(self.s)


    def __str__(self) -> str:
        return f"BEJÁRAT: {str(self.s)[1:-1]}"


def main():
    s = Sor()
    print(s)         
    print(s.ures())  
    s.betesz(1)
    s.betesz(4)
    s.betesz(5)
    print(s)         
    print(s.meret()) 
    print(s.ures())  
    x = s.kivesz()
    print(x)         
    print(s)         
    s.kivesz()
    print(s)
    s.kivesz()       
    x = s.kivesz()
    print(x)         


if __name__ == "__main__":
    main()