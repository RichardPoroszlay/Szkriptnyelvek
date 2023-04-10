#!/usr/bin/env python3


"""
Ebben az állományban a Verem adatszerkezet implementációját valósítom meg.
"""


class Verem:
    def __init__(self):
        self.v = []

    
    def betesz(self, n: int):
        self.v.append(n)
    

    def kivesz(self) -> int:
        if len(self.v) == 0:
            return None
        return self.v.pop(-1)

    
    def ures(self) -> bool:
        if len(self.v) == 0:
            return True
        return False
    

    def meret(self) -> int:
        return len(self.v)


    def __str__(self) -> str:
        return f"[{str(self.v)[1:-1]}"
    

def main():
    # test
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1, 4, 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1, 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)
        

if __name__ == "__main__":
    main()