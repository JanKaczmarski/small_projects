szukanaLiczba = 40

zgadywanaLiczba = 0

while szukanaLiczba != zgadywanaLiczba :

    zgadywanaLiczba = int(input("Odgadnij liczbę: "))
    
    if(zgadywanaLiczba > szukanaLiczba):
        print("Za duża")
    elif(zgadywanaLiczba < szukanaLiczba):
        print("Za mała")
    else:
        print("Brawoo")
        
