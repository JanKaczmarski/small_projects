numbers = [14, 15, 16, 17, 18, 19, 20]

print(numbers)

print("1 - Zakończ program")
print("2 - podnieść do drugiej potęgi.")
print("3 - podnieść do trzeciej potęgi.")




while(True):
    wybor = input("Do której potęgi chcesz podnieść dane liczby?")
    if (wybor == '2'):
        doublePoweredNumbers = {
            number : number**2
            for number in numbers 
                                }
        print(doublePoweredNumbers)
    elif (wybor == '3'):
        triplePoweredNumbers = {
            number : number**3
            for number in numbers
                                }
        print(triplePoweredNumbers)
    elif (wybor == '1'):
        print("Zakończono program.")
        break
    else:
        print("Wybrano złą operację. Ponów próbę.")
        
