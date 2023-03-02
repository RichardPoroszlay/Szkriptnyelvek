#!/usr/bin/env python3

# 3. óra - Listák (dinamikus tömbök)
# Listánál szeletelés eredménye mindig egy új objektum lesz
# a = [1, 3, 4]
# b = a
# b[0] = 100 esetén a[0] is 100 lesz, mivel b csak egy referencia

# ha másolatot szeretnénk a-ról b-be, akkor szeleteljük a komplett a listát:    b = a[:]
# for ciklusban a ciklusváltozó egy másolat
# list(content) függvény
# in operator
# .extend()


def main():
    html = """
        <html>
        <body>
        <h1>hello</h1>
        </body>
        </html>    
        """.strip()
    print("'" + html + "'") # sortörés a string elején és végén (ha nincsen.strip())


if __name__ == "__main__":
    main()