#!/usr/bin/env python3


"""
A feladatunk az, hogy kapunk egy kifejezést, melyben szerepelhetnek számok, zárójelek, operátorok.
Minket csak a zárójelek érdekelnek. Háromféle zárójel szerepelhet egy kifejezésben.
Ha egy zárójelet megnyitunk, akkor a típusának megfelelő párral be is kell zárni.

Egy függvény segítségével eldöntjük egy kifejezésről a zárójelek alapján, hogy valid-e vagy sem.

Segítségünkre lesz a feladatunk megoldásában a stack adatszerkezet.
Ha végigértünk az összes karakteren, s a verem üres, akkor a zárójelezés helyes, másképp hibás.
"""


def zarojel_checker(kifejezes):
    nyito = ["(", "{", "["]
    zaro = [")", "}", "]"]
    stack = []

    for char in kifejezes:
        if char in nyito:
            stack.append(char)
        elif char in zaro:
            if not stack or nyito.index(stack.pop()) != zaro.index(char):
                return "Is valid: " + str(False)

    return "Is valid: " + str((not stack))


def main():
    # test
    print(zarojel_checker("(5+3)*2+1"))
    print(zarojel_checker("{[(3+1)+2]+}"))
    print(zarojel_checker("(3+{1-1)}"))
    print(zarojel_checker("[1+1]+(2*2)-{3/3}"))
    print(zarojel_checker("(({[(((1)-2)+3)-3]/3}-3)"))


if __name__ == "__main__":
    main()