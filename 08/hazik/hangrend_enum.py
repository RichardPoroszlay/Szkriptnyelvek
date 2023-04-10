#!/usr/bin/env python3


"""
Ebben a programban a korábbi hangrendes feladatot oldjuk meg ismét, ezúttál Enum segítségével.
"""


from enum import Enum


class Hangrend(Enum):
    MELY = "aáoóuú"
    MAGAS = "eéiíöőüű"


def hangrend_kitalalo(szavak) -> str:
    hangrendek = []
    
    for szó in szavak:
        mely_betu = 0
        magas_betu = 0
        for betű in szó:
            if betű in Hangrend.MELY.value:
                mely_betu += 1
            elif betű in Hangrend.MAGAS.value:
                magas_betu += 1
        if mely_betu > 0 and magas_betu > 0:
            hangrendek.append("A(z) " + szó + " szó vegyes hangrendű!")
        elif mely_betu > 0 and magas_betu == 0:
            hangrendek.append("A(z) " + szó + " szó mély hangrendű!")
        elif mely_betu == 0 and magas_betu > 0:
            hangrendek.append("A(z) " + szó + " szó magas hangrendű!")
        else:
            hangrendek.append("A(z) " + szó + " szó semmilyen hangrendű!")
    
    eredmeny: str = "\n".join(hangrendek)
    return eredmeny


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "pffff"]
    print(hangrend_kitalalo(words))


if __name__ == "__main__":
    main()