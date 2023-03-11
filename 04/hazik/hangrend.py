#!/usr/bin/env python3


MELY_MGHK = "aáoóuú"
MAGAS_MGHK = "eéiíöőüű"


def hangrend_kitalalo(szavak):
    hangrendek = []
    
    for szó in szavak:
        mely_betu = 0
        magas_betu = 0
        for betű in szó:
            if betű in MELY_MGHK:
                mely_betu += 1
            elif betű in MAGAS_MGHK:
                magas_betu += 1
        if mely_betu > 0 and magas_betu > 0:
            hangrendek.append("A(z) " + szó + " szó vegyes hangrendű!")
        elif mely_betu > 0 and magas_betu == 0:
            hangrendek.append("A(z) " + szó + " szó mély hangrendű!")
        elif mely_betu == 0 and magas_betu > 0:
            hangrendek.append("A(z) " + szó + " szó magas hangrendű!")
        else:
            hangrendek.append("A(z) " + szó + " szó semmilyen hangrendű!")
    
    eredmeny = "\n".join(hangrendek)
    return eredmeny


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "pffff"]
    print(hangrend_kitalalo(words))


if __name__ == "__main__":
    main()