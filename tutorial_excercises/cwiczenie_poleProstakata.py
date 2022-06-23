def poleProstokata(a, b):
    return (a * b)
def poleKwadratu(a):
    return (a*a)
def poleTrojkata(a, h):
    return ((a * h)/2)
def poleTrapezu(a, b, h):
    return (((a + b)*h)/2)
def poleKola(r):
    return((r*r)*3.14)

#wybor = input("1 - pole prostokąta, 2 - pole kwadratu, 3 - pole trójkąta, 4 - pole trapezu, 5 - pole koła, 6 - zakończ program ")
print("Menu")
print('1 - pole prostokąta')
print('2 - pole kwadratu')
print('3 - pole trójkąta')
print('4 - pole trapezu')
print('5 - pole koła')
print('6 - zakończ program')

while(True):
    wybor = input("Podaj pole której figury chcesz obliczyć:")
    if (wybor == '1'):
        a = float(input("Podaj bok a:"))
        b = float(input("Podaj bok b:"))
        print("Pole prostokąta wynosi:", poleProstokata(a, b))
    elif (wybor == '2'):
        a = float(input("Podaj bok a:"))
        print("Pole kwadratu wynosi:", poleKwadratu(a))
    elif (wybor == '3'):
        a = float(input("Podaj podstawę trójkąta: "))
        h = float(input("Podaj wysokość trójkąta: "))
        print("Pole trójkąta wynosi:", poleTrojkata(a, h))
    elif (wybor == '4'):
        a = float(input("Podaj pierwszą podstawę trapezu: "))
        b = float(input("Podaj drugą podstawę trapezu: "))
        h = float(input("Podaj wysokość trapezu: "))
        print("Pole trapezu wynosi:", poleTrapezu(a, b, h))
    elif (wybor == '5'):
        r = float(input("Podaj promień koła: "))
        print("Pole koła wynosi:", poleKola(r))
    elif(wybor == '6'):
        print("Koniec programu")
        break
    else:
        print("Podałeś niewłaściwe dane, ponów wybór działania.")
