slownik = {}


while (True):
    wybor = input('Wybierz którą operację chcesz wykonać: a - dodać nową definicję, b - wyszukać istniejącą definicję, c - usunąć wybraną definicję, d - zakończyć program:')

    if (wybor == 'a'):
        klucz = input("Podaj klucz (słowo) do zdefiniowania: ")
        definicja = input("Podaj definicję: ")
        slownik[klucz] = definicja
        print("Definicja dodana pomyślnie")
    elif(wybor == 'b'):
        klucz = input("Czego szukasz? ")
        if klucz in slownik:
            print(slownik[klucz])
        else:
            print("Nie ma takiego klucza.")
    elif (wybor == 'd'):
        print("Koniec programu.")
        break
    elif(wybor == 'c'):
        klucz = input("Podaj jaki klucz chcesz usunąć: ")
        if klucz in slownik:
            del slownik[klucz]
            print("Usunięto klucz o nazwie:", klucz)
        else:
            print("Nie ma klucza o nazwie:", klucz)
    else:
        print("Podałeś niewłaściwą literkę.")
