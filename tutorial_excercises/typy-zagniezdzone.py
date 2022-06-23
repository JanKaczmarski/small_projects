# TYPY ZAGNIEŻDZONE, wypisanie wartości

imie = "Arkadiusz"
wiek = 29
plec = "mężczyzna"

imie2 = "Wioletta"
wiek2 = 23
plec2 = "kobieta"


osoba1 = ('Arkadiusz', 29, 'mężczyzna')
osoba2 = ('Wioletta', 23, 'kobieta')
osoba3 = ('Kuba', 33, 'mężczyzna')
 
listaGosci = {
                ('Arkadiusz', 28, 'mężczyzna', '577 022 192'),
                ('Wioletta', 22, 'kobieta', '108 970 693'),
                ('Kuba', 32, 'mężczyzna', '652 468 369')  
             }
listaGosci2 = {
                ('Arkadiusz', 28, 'mężczyzna', '577 022 192'),
                ('W', 22, 'kobieta', '512 068 054'),
                ('K', 32, 'mężczyzna', '885 500 333')  
             }

listaGosci3 = listaGosci | listaGosci2

for imie, wiek, plec, telefon in listaGosci3:
    print("Imię:", imie)
    print("Wiek:", wiek)
    print("Płeć:", plec)
    print("Numer telefonu:", telefon)
    print("\n")



"""
for imie, wiek, plec, telefon in listaGosci:
    print("Imię:", imie)
    print("Wiek:", wiek)
    print("Płeć:", plec)
    print("Numer telefonu:", telefon)
    print("\n")
"""

 

 
