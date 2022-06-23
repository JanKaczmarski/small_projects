import random


def losowanieSzesciuLiczb(choosenNumbers):
    
    while(True):
        numbersList = [element
                    for element in range(50)
                    ]
        i = 0
        winningNumbersList = []
        while i < 6:
            winningNumber = random.choice(numbersList)
            winningNumbersList.append(winningNumber)
            numbersList.remove(winningNumber)
            i = i + 1
        print("Wylosowane liczby to:", winningNumbersList)
        if (winningNumbersList == choosenNumbers):
            print("Wygrałeś 6 w lotto.")
            break
        
        


print(losowanieSzesciuLiczb([23, 26, 36, 32, 47, 8]))


