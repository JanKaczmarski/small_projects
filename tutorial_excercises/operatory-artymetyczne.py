"""
+ dodawanie
- odejmowanie
* mnożenie
/ dzielenie

() - jak w matematyce kierują kolejnością działania

** potęgowanie
// dzielenie w "dół"
% - modulo (reszta z dzielenia)


"""

#Ćwiczenie z vatem

vat = 23
obliczonyVat = (1 + vat / 100)

cenaNettoTelewizora = 1000
cenaNettoDrukarki = 200
cenaNettoPapierosow = 10

cenaBruttoTlewizora = cenaNettoTelewizora * obliczonyVat
cenaBruttoDrukarki = cenaNettoDrukarki * obliczonyVat
cenaBruttoPapierosow = cenaNettoPapierosow * obliczonyVat

print("Cena brutto telewizora:")
print(cenaBruttoTlewizora)
print("Cena brutto drukarki:")
print(cenaBruttoDrukarki)
print("Cena brutto papierosow:")
print(cenaBruttoPapierosow)
