wybor = input("Wybier działanie: * - mnożenie, / - dzielenie, + - dodawanie, - - odejmowanie, ** - potęgowanie: ")
a = int(input("Wprowadź pierwszą liczbę: "))
b = int(input("Wprowadź drugą liczbę: "))


mnozenie = a * b
dodawanie = a + b
odejmowanie = a - b
potegowanie = a ** b

"""
if(liczba < 0):
    print("Wartość bezwględna z", liczba, "wynosi: ",liczba * -1)
elif(liczba > 0):
    print("Wartość bezwględna z", liczba, "wynosi: ",liczba)
else:
    print("Wartość bezwględna z 0 wynosi: 0")
"""
if(wybor == '*'):
    if(mnozenie < 0):
        print("wartość bezwględna z tego działania wynosi: ",mnozenie * -1)
    elif():
        print(mnozenie)
elif(wybor == '/'):
    if(b == 0):
        print("Nie dziel przez zero")
    else:
        if((a / b) < 0):
            print("wartość bezwględna z tego działania wynosi: ",(a / b) * -1)
        else:
            print(dzielenie)
elif(wybor == '+'):
    if(dodawanie < 0):
        print("wartość bezwględna z tego działania wynosi: ",dodawanie * -1)
    else:
        print(dodawanie)
elif(wybor == '-'):
    if(odejmowanie < 0):
        print("wartość bezwględna z tego działania wynosi: ",odejmowanie * -1)
    else:
        print(odejmowanie)
elif(wybor == '**'):
    if(potegowanie < 0):
        print("wartość bezwględna z tego działania wynosi: ",potegowanie * -1)
    else:
        print(potegowanie)
        
