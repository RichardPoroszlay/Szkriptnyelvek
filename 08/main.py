#!/usr/bin/env python3

# OO-ról lesz szó
# Pythonban nincsen 'new' operator
# Metódus definiálásánál kötelező kitenni a selfet, példányosításnál nem muszáj
# Pythonban is van egy object osztály, ez az ősosztály (kicsi betűvel kezdődik)
# Minden publikus Pythonban

# Container osztály: tárolásra szolgáló osztály
# Azok az elemek, amelyek előtt 1 db _ jel van, azt privátként kéne kezelni
# pl. _spam

# Pythonban vannak speciális metódusok, ezeknek a nevük __ kezdődik és végződik
# Pl. __init__, __str__, __name__
# Angolul ezeket "magic methods"-nak is nevezik
# Ezekkel pl. megvalósítható az operator overloading


# üres osztály
class EmptyClass:
    pass


class MyClass:
    def hello(self):    # a self az egy olyan referencia, ami az aktuális objektumra mutat (Javaban ez this)
        return "hello world"


class Hello():
    def create_name(self, name):    # itt is látható, hogy az első paraméter kötelezően a self
        self.name = name    # létrejön a self.name változó, nem kell előre definiálni


    def display_name(self):
        return self.name


    def greet(self):
        print(f"Hello {self.name}")


class Greetings:
    def __init__(self, name):   # konstruktor
        self.name = name  


    def say_hi(self):
        print(f"Hi {self.name}!")


class Bag:
    def __init__(self):
        self.data = []
    

    def add(self, n):
        self.data.append(n)
    

    def __str__(self):  # ez olyan, mint a toString() Javaban
        return f"Bag({str(self.data)})"
    

    def add_twice(self, n):
        self.add(n)
        self.add(n)


class Counter:
    counter = 0 # osztályváltozó

    def __init__(self):
        Counter.counter += 1

    
    def hello(self):
        print("hello")


def main():
    o1 = EmptyClass()    # osztály példányosítása
    o2 = MyClass()  # a self az o2 objektumra mutat adott esetben
    print(o2.hello())

    h = Hello()
    h.create_name("Alice")
    print(h.name)   # h-nak a name nevű objektumára hivatkozunk
    print(h.display_name())
    h.greet()

    g = Greetings("Alice")  # konstruktor hívás
    g.say_hi()

    b = Bag()
    b.add(5)
    print(b)

    c1 = Counter()
    c2 = Counter()
    c3 = Counter()
    print(Counter.counter)


if __name__ == "__main__":
    main()