from enum import Enum
Menu_Dzialania = Enum('Menu_Dzialania', {'dodawanie':'+',  'odejmowanie':'-',  'mnozenie':'*', 'dzielenie':'/', 'koniec':'#'})







while(True):
    wybor = input("+ - dodawanie, - - odjemowanie, * - mnożenie, / - dzielenie, # - zakończ program")


    if (wybor == Menu_Dzialania.dodawanie.value):
        a = int(input('Podaj pierwszą liczbę: '))
        b = int(input('Podaj druga liczbę: '))

        print(a + b)
    elif(wybor == Menu_Dzialania.odejmowanie.value):
        a = int(input('Podaj pierwszą liczbę: '))
        b = int(input('Podaj druga liczbę: '))

        print(a - b)
    elif(wybor == Menu_Dzialania.mnozenie.value):
        a = int(input('Podaj pierwszą liczbę: '))
        b = int(input('Podaj druga liczbę: '))

        print(a * b)
    elif(wybor == Menu_Dzialania.dzielenie.value):
        a = int(input('Podaj pierwszą liczbę: '))
        b = int(input('Podaj druga liczbę: '))

        if (b == 0):
            print('Nie dizel przez zero.')
        else:
            print(a/b)
    elif(wybor == Menu_Dzialania.koniec.value):
        print("Koniec programu")
        break
    else:
        print("Wybrałeś niewłaściwe działanie. Spróbuj ponownie.")
