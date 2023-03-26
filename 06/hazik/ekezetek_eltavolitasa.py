#/usr/bin/env python3

"""
Ebben a programban egy szöveget fogunk lekezelni: az ékezetes karakterekből
ékezet nélküli karakterekre fogjuk lecserélni.
"""


TEXT = """A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata. 
A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során. 
A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre."""


def modifier(text):
    """
    Szótár segítségével kicseréljük az ékezetes karaktereket ékezet nélküliekre.
    Az eredmény szavakat egy listában tároljuk, melyet a végén joinolunk, hogy megkapjuk a kész szöveget, amelyet visszaad a függvény.
    """
    d = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ő": "o",
        "ö": "o",
        "ú": "u",
        "ű": "u",
        "ü": "u"
    }

    result = []
    for word in text.split():
        for c in word:
            if c in d.keys():
                word = word.replace(c, d.get(c))
        result.append(word)
    
    return " ".join(result)
    

def main():
    print('\n' + modifier(TEXT))


if __name__ == "__main__":
    main()