wybor = input("Wybier działanie: * - mnożenie, / - dzielenie, + - dodawanie, - - odejmowanie, ** - potęgowanie, % - modulo: ")

a = int(input("Wybierz pierwszą liczbę: "))
b = int(input("Wybierz drugą liczbę: "))
c = int(input("Wybierz pierwszą liczbę: "))
d = int(input("Wybierz pierwszą liczbę: "))
e = int(input("Wybierz pierwszą liczbę: "))
f = int(input("Wybierz drugą liczbę: "))
g = int(input("Wybierz pierwszą liczbę: "))
h = int(input("Wybierz pierwszą liczbę: "))

    

if(wybor == '*'):
    print(a * b)
elif(wybor == '/'):
    if(b == 0):
        print("Nie dziel przez zero.")
    elif(b != 0):
        print(a / b)
elif(wybor == '+'):
    print(a + b + c + d + e + f + g + h)
elif(wybor == '-'):
    print(a - b)
elif(wybor == '**'):
    print(a ** b)
elif(wybor == '%'):
    print(a % b)
else:
    print("Nie wybrałeś dobrego działania.")
    

