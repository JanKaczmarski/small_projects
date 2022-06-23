

wynik = 0

i = 0

while i < 3:
    x = int(input("Podaj liczbę parzystą: "))
    if (x % 2 == 0):
        wynik += x
    else:
        print("Podałeś liczbę nieprazystą. Podaj liczbę parzystą.")
        continue
    print("aktualny wynik dodawania to:", wynik)
